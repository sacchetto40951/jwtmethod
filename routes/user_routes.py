from flask import Blueprint, request, jsonify
from flask_jwt_extended import get_jwt_identity, jwt_required
from controllers.user_controller import UserController 

user_bp = Blueprint('users', __name__)

@user_bp.route('/', methods=['POST'])
@user_bp.route('/register', methods=['POST'])
def register():
    response, status = UserController.register_user(request.get_json() or {})
    return jsonify(response), status

@user_bp.route('/login', methods=['POST'])
def login():
    response, status = UserController.login_user(request.get_json() or {})
    return jsonify(response), status

@user_bp.route('/me', methods=['GET'])
@jwt_required()
def get_current_user():
    response, status = UserController.get_user(get_jwt_identity())
    return jsonify(response), status

@user_bp.route('/me', methods=['PUT'])
@jwt_required()
def update_current_user():
    response, status = UserController.update_user(
        get_jwt_identity(), request.get_json() or {}
    )
    return jsonify(response), status

@user_bp.route('/me', methods=['DELETE'])
@jwt_required()
def delete_current_user():
    response, status = UserController.delete_user(get_jwt_identity())
    return jsonify(response), status

@user_bp.route('/<int:user_id>', methods=['GET'])
@jwt_required()
def get_user(user_id):
    response, status = UserController.get_user(user_id)
    return jsonify(response), status

@user_bp.route('/<int:user_id>', methods=['PUT'])
@jwt_required()
def update_user(user_id):
    response, status = UserController.update_user(user_id, request.get_json() or {})
    return jsonify(response), status

@user_bp.route('/<int:user_id>', methods=['DELETE'])
@jwt_required()
def delete_user(user_id):
    response, status = UserController.delete_user(user_id)
    return jsonify(response), status
