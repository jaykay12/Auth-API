from os import environ

class DevelopmentConfig(object):
    DEBUG = True
    SECRET_KEY = environ.get('SECRET_KEY')

    SQLALCHEMY_DATABASE_URI = environ.get("DEVELOPMENT_DATABASE_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True

class StageConfig(object):
    SECRET_KEY = environ.get('SECRET_KEY')

    SQLALCHEMY_DATABASE_URI = environ.get("STAGE_DATABASE_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True

class ProductionConfig(object):
    SECRET_KEY = environ.get('SECRET_KEY')

    SQLALCHEMY_DATABASE_URI = environ.get("PRODUCTION_DATABASE_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True

class TestConfig(object):
    SECRET_KEY = environ.get('SECRET_KEY')

    SQLALCHEMY_DATABASE_URI = environ.get("TESTING_DATABASE_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True

class oAuthConfig(object):
    OAUTH_CREDENTIALS = {
        "facebook": {
                "id": environ.get("FACEBOOK_APP_ID"),
                "secret": environ.get("FACEBOOK_APP_SECRET")
                },
        "twitter": {
                "id": environ.get("TWITTER_API_KEY"),
                "secret": environ.get("TWITTER_API_SECRET")
        },
        "github": {
                "id": environ.get("GITHUB_CLIENT_ID"),
                "secret": environ.get("GITHUB_CLIENT_SECRET")
        },
        "google": {
                "id": environ.get("GOOGLE_CLIENT_ID"),
                "secret": environ.get("GOOGLE_CLIENT_SECRET")
        },
        "linkedin": {
                "id": environ.get("LINKEDIN_CLIENT_ID"),
                "secret": environ.get("LINKEDIN_CLIENT_SECRET")
        }
    }
