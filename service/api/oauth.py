import json

from rauth import OAuth1Service, OAuth2Service
from flask import current_app, url_for, request, redirect, session

class OAuthSignIn(object):
    providers = None

    def __init__(self, provider_name):
        self.provider_name = provider_name
        credential = current_app.config['OAUTH_CREDENTIALS'][provider_name]
        self.consumer_id = credential['id']
        self.consumer_secret = credential['secret']

    def authorize(self):
        pass

    def callback(self):
        pass

    def get_callback_url(self):
        return url_for('oauth_callback', provider=self.provider_name, _external=True)

    @classmethod
    def load_provider(self):
        if self.providers is None:
            self.providers = {}
            for provider_class in self.__subclasses__():
                provider = provider_class()
                self.providers[provider.provider_name] = provider

    @classmethod
    def get_provider(self, provider_name):
        self.load_provider()
        return self.providers[provider_name]

class FacebookSignIn(OAuthSignIn):
    def __init__(self):
        super(FacebookSignIn, self).__init__('facebook')
        self.service = OAuth2Service(
                    name = 'facebook',
                    client_id = self.consumer_id,
                    client_secret = self.consumer_secret,
                    authorize_url = 'https://graph.facebook.com/oauth/authorize',
                    access_token_url = 'https://graph.facebook.com/oauth/access_token',
                    base_url = 'https://graph.facebook.com/'
        )

    def authorize(self):
        params = {
            'scope': 'email',
            'response_type': 'code',
            'redirect_uri': self.get_callback_url()
        }
        return redirect(self.service.get_authorize_url(**params))

    def callback(self):
        def decode_json(payload):
            return json.loads(payload.decode('utf-8'))

        if 'code' not in request.args:
            return None,None,None
        data = {
            'code': request.args['code'],
            'grant_type': 'authorization_code',
            'redirect_uri': self.get_callback_url()
        }
        oauth_session = self.service.get_auth_session(data = data, decoder = decode_json)
        me = oauth_session.get('me?fields=id,email').json()

        return ('facebook$' + me['id'], me['email'].split('@')[0], me['email'])

class TwitterSignIn(OAuthSignIn):
    def __init__(self):
        super(TwitterSignIn, self).__init__('twitter')
        self.service = OAuth1Service(
                    name = 'twitter',
                    consumer_key=self.consumer_id,
                    consumer_secret=self.consumer_secret,
                    request_token_url='https://api.twitter.com/oauth/request_token',
                    authorize_url = 'https://api.twitter.com/oauth/authorize',
                    access_token_url = 'https://api.twitter.com/oauth/access_token',
                    base_url = 'https://api.twitter.com/1.1/'
        )

    def authorize(self):
        params = {
            'oauth_callback': self.get_callback_url()
        }
        request_token = self.service.get_request_token(params = params)

        session['request_token'] = request_token
        return redirect(self.service.get_authorize_url(request_token[0]))

    def callback(self):
        request_token = session['request_token']
        if 'oauth_verifier' not in request.args:
            return None, None, None
        oauth_session = self.service.get_auth_session(request_token[0],request_token[1],
            data={'oauth_verifier': request.args['oauth_verifier']}
        )

        me = oauth_session.get('account/verify_credentials.json').json()
        print(me)

        return ('twitter$' + str(me['id']), me['screen_name'], None)

class GithubSignIn(OAuthSignIn):
    def __init__(self):
        super(GithubSignIn, self).__init__('github')
        self.service = OAuth2Service(
                    name = 'github',
                    client_id = self.consumer_id,
                    client_secret = self.consumer_secret,
                    authorize_url = 'https://github.com/login/oauth/authorize',
                    access_token_url = 'https://github.com/login/oauth/access_token',
                    base_url = 'https://api.github.com/'
        )

    def authorize(self):
        params = {
            'scope': 'user',
            'redirect_uri': self.get_callback_url()
        }
        return redirect(self.service.get_authorize_url(**params))

    def callback(self):

        if 'code' not in request.args:
            return None,None,None
        data = {
            'code': request.args['code'],
            'grant_type': 'authorization_code',
            'redirect_uri': self.get_callback_url()
        }
        oauth_session = self.service.get_auth_session(data = data)
        me = oauth_session.get('user').json()

        return ('github$' + str(me['id']), str(me['login']), str(me['email']))
