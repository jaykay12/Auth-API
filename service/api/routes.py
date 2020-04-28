from flask import abort, jsonify, request, g
from flask import current_app as app
from .models import db, User
from .auth import auth

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

@app.route('/api/token')
@auth.login_required
def get_auth_token():
    token = g.user.generate_auth_token(600)
    return (jsonify({'token': token.decode('ascii'), 'duration': 600}), 200)

@app.route('/api/resource')
@auth.login_required
def get_resource():
    return (jsonify({'data': 'Hello, %s!' % g.user.username}), 200)
