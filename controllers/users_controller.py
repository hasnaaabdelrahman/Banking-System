from flask import Flask, request , Blueprint, jsonify

from services.user_services import UserService
from repositories.user_repository import UserRepository
from database import db

user_bp= Blueprint('users', __name__)

user_repository = UserRepository(db.session)
user_service = UserService(user_repository)

@user_bp.route("/register" , methods=["POST"])
def register():
    data = request.json
    user = user_service.register(data)
    return jsonify(user), 201

@user_bp.route("/login" , methods=["POST"])
def login():
    data = request.json
    user = user_service.login(data['username'], data['password'])
    return jsonify(user), 200