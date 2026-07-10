from flask import Flask, request , Blueprint, jsonify

from services.bank_account_services import BankAccountService
from repositories.bank_account_repository import BankAccountRepository
from database.db import session

bank_bp = Blueprint('bank_account', __name__)

bank_account_repository = BankAccountRepository(session)
bank_account_service = BankAccountService(bank_account_repository)

@bank_bp.route('/bank_account', methods=['POST'])
def create_bank_account():
    data = request.json
    bank_account = bank_account_service.create_bank_account(data)
    return jsonify(bank_account), 201

@bank_bp.route('/bank_account/<str:id>', methods=['GET'])
def get_bank_account(id:str):
    bank_account = bank_account_service.get_by_id(id)
    return jsonify(bank_account), 200

@bank_bp.get('/user/<str:user_id>/bank_account', methods=['GET'])
def get_user_bank_account(user_id:str):
    bank_account = bank_account_service.get_by_user_id(user_id)
    return jsonify(bank_account), 200

@bank_bp.put('/bank_account/<str:id>', methods=['PUT'])
def update_bank_account(id:str):
    bank_account = bank_account_service.update_by_id(id)
    return jsonify(bank_account), 200

@bank_bp.delete('/bank_account/<str:id>', methods=['DELETE'])
def delete_bank_account(id:str):
    bank_account_service.delete_by_id(id)
    return '', 204
