from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity
from models import User, Project
from utils import hash_password, verify_password

# Blueprints
auth_bp = Blueprint('auth', __name__)
project_bp = Blueprint('projects', __name__)

# User Registration
@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    role = data.get('role', 'user')  # Default role is "user"

    if role not in ['admin', 'user']:
        return jsonify({'error': 'Invalid role'}), 400

    if User.objects(username=username).first():
        return jsonify({'error': 'User already exists'}), 400

    hashed_password = hash_password(password)
    User(username=username, password=hashed_password, role=role).save()

    return jsonify({'message': 'User registered successfully'}), 201

# User Login
@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user = User.objects(username=username).first()
    if not user or not verify_password(user.password, password):
        return jsonify({'error': 'Invalid credentials'}), 401

    token = create_access_token(identity={'username': user.username, 'role': user.role})
    return jsonify({'access_token': token}), 200

# Get all projects (accessible to all users)
@project_bp.route('/projects', methods=['GET'])
@jwt_required()
def get_projects():
    projects = Project.objects()
    return jsonify(projects), 200

# Create a project (admin only)
@project_bp.route('/projects', methods=['POST'])
@jwt_required()
def create_project():
    current_user = get_jwt_identity()
    if current_user['role'] != 'admin':
        return jsonify({'error': 'Admin access required'}), 403

    data = request.get_json()
    name = data.get('name')
    description = data.get('description')

    Project(name=name, description=description, created_by=current_user['username']).save()
    return jsonify({'message': 'Project created successfully'}), 201
