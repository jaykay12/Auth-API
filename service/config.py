class Config(object):
    DEBUG = True
    SECRET_KEY = 'the quick brown fox jumps over the lazy dog'

    SQLALCHEMY_DATABASE_URI = 'sqlite:///auth.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
