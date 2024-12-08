from bcrypt import hashpw, gensalt, checkpw

def hash_password(password):
    return hashpw(password.encode('utf-8'), gensalt()).decode('utf-8')

def verify_password(hashed_password, password):
    return checkpw(password.encode('utf-8'), hashed_password.encode('utf-8'))
