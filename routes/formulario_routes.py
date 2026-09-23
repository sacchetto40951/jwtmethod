from flask import Blueprint, request, jsonify  
from flask_jwt_extended import jwt_required, get_jwt_identity  
from controllers.formulario_controller import (
    FormularioController,
    formulario_get
) 

formulario_bp = Blueprint('formularios', __name__)

@formulario_bp.route('/', methods=['POST'])
@jwt_required() 
def create_formulario():
    user_id = get_jwt_identity()
    return jsonify(FormularioController.create_formulario(user_id, request.get_json()))

@formulario_bp.route('/form', methods=['GET'])
@jwt_required()
def get_formulario(id):
    return formulario_get(id)