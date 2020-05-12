from flask import current_app as app
from flask import redirect, jsonify, request, flash
from .oauth import OAuthSignIn
from .models import db, User
from flask_login import current_user, login_user
from .log import accesslogger

@app.route('/oauth/')
def index():
    response = dict()
    response["info"]="Basic oAuth API"
    response["developer"]="Jalaz Kumar"
    response['providers']=str(OAuthSignIn.providers)
    accesslogger.info("Accessed: oAuth API Introduction")
    return (jsonify(response), 200)

@app.route('/oauth/authorize/<provider>')
def oauth_authorize(provider):
    oauth = OAuthSignIn.get_provider(provider)
    return oauth.authorize()

@app.route('/oauth/callback/<provider>')
def oauth_callback(provider):
    oauth = OAuthSignIn.get_provider(provider)
    id, username, email = oauth.callback()
    if id is None:
        return redirect('/oauth/failure/'+str(provider), 302)

    user = User.query.filter_by(id=id).first()
    if not user:
        user = User(id=id, username=username, email=email)
        try:
            db.session.add(user)
            db.session.commit()
        except:
            db.session.rollback()
            return redirect('/oauth/failure/'+str(provider), 302)
    return redirect('/oauth/success/'+str(provider), 302)

@app.route('/oauth/failure/<provider>')
def oauth_failure(provider):
    flash("oAuth Failed")
    return (jsonify({"message":"DB Error / Not Authorized"}), 503)

@app.route('/oauth/success/<provider>')
def oauth_success(provider):
    flash("oAuth Success")
    return (jsonify({"message":"oAuth Success"}), 200)
