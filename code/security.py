from werkzeug.security import safe_str_cmp
from user import User
users = [
    User(1,"simoel33","password")
]

# https://pythonhosted.org/Flask-JWT/ documentation pour jwt authentication
username_mapping = {u.username: u for u in users}
userid_maping = {u.id : u for u in users}

def authenticate(username,password):
    user = username_mapping.get(username,None)
    if user and safe_str_cmp(user.password.encode('utf-8'), password.encode('utf-8')):
            return user

def identity(payload):
    user_id = payload['identity']
    return userid_maping.get(user_id,None)
    