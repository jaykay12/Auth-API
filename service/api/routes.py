from flask import abort, jsonify, request, g
from flask_httpauth import HTTPBasicAuth
from flask import current_app as app
from .models import db, User

auth = HTTPBasicAuth()

@auth.verify_password
def verify_password(username, password):
    user = User.query.filter_by(username = username).first()
    if not user or not user.verify_password(password):
        return False
    g.user = user
    return True

@app.route('/api/')
def intro():
    response = dict()
    response["info"]="Basic Auth API"
    response["developer"]="Jalaz Kumar"
    return (jsonify(response), 200)

@app.route('/api/users', methods=['POST'])
def register_user():
    id = request.json.get('id')
    username = request.json.get('username')
    password = request.json.get('password')
    if id is None or username is None or password is None:
        abort(400)
    user = User(id=int(id),username=username)
    user.hash_password(password)
    db.session.add(user)
    db.session.commit()
    return (jsonify({'username': user.username}), 201)

@app.route('/api/users/<int:id>')
def get_user(id):
    user = User.query.get(id)
    if not user:
        abort(400)
    return (jsonify({'username': user.username}), 200)

@app.route('/api/resource')
@auth.login_required
def get_resource():
    return (jsonify({'data': 'Hello, %s!' % g.user.username}), 200)
