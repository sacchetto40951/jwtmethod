from flask import Blueprint, request, jsonify  
from flask_jwt_extended import jwt_required, get_jwt_identity  
from controllers.formulario_controller import (
    FormularioController
) 

formulario_bp = Blueprint('formularios', __name__)

@formulario_bp.route('/', methods=['POST'])
@jwt_required() 
def create_formulario():
    user_id = get_jwt_identity()
    response, status = FormularioController.create_formulario(
        user_id, request.get_json() or {}
    )
    return jsonify(response), status

@formulario_bp.route('/<int:formulario_id>', methods=['GET'])
@jwt_required()
def get_formulario(formulario_id):
    response, status = FormularioController.get_formulario(formulario_id)
    return jsonify(response), status

@formulario_bp.route('/<int:formulario_id>', methods=['PUT'])
@jwt_required()
def update_formulario(formulario_id):
    response, status = FormularioController.update_formulario(
        formulario_id, request.get_json() or {}
    )
    return jsonify(response), status

@formulario_bp.route('/<int:formulario_id>', methods=['DELETE'])
@jwt_required()
def delete_formulario(formulario_id):
    response, status = FormularioController.delete_formulario(formulario_id)
    return jsonify(response), status