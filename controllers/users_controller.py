from flask import Flask, request , Blueprint, jsonify

from schemas.user_schema import UserRegisterSchema, UserLoginSchema
from services.user_services import UserService
from repositories.user_repository import UserRepository
from database import db

user_bp= Blueprint('users', __name__)

user_repository = UserRepository(db.session)
user_service = UserService(user_repository)

@user_bp.route("/register" , methods=["POST"])
def register():
    data = request.json
    user_data = UserRegisterSchema(**data)
    user = user_service.register(user_data)
    return jsonify(user), 201

@user_bp.route("/login" , methods=["POST"])
def login():
    data = request.json
    user_data = UserLoginSchema(**data)
    user = user_service.login(user_data)
    return jsonify(user), 200