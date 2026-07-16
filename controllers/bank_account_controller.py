from flask import Flask, request , Blueprint, jsonify

from exceptions.bank_account_exceptions import BankAccountNotFound, BankAccountAlreadyExists
from schemas.bank_account_schema import BankAccountSchema
from services.bank_account_services import BankAccountService
from repositories.bank_account_repository import BankAccountRepository
from database.db import session

bank_bp = Blueprint('bank_account', __name__)

bank_account_repository = BankAccountRepository(session)
bank_account_service = BankAccountService(bank_account_repository)

@bank_bp.route('/bank_account', methods=['POST'])
def create_bank_account():
    try:
        data = request.json
        account_data = BankAccountSchema(**data)
        bank_account = bank_account_service.create_bank_account(account_data)
        return jsonify({
            "message": "Bank account created",
            "bank account": {
                "id": bank_account.id,
                "account_number": bank_account.account_number,
                "account_type": bank_account.account_type.value,
                "is_active": bank_account.is_active,
                "balance": bank_account.balance,
                "user_id": bank_account.user_id,
            }
        }), 201
    except BankAccountAlreadyExists as e:
        return jsonify({"message": str(e)}), 409

@bank_bp.route('/bank_account/<string:id>', methods=['GET'])
def get_bank_account(id:str):
    try:
        bank_account = bank_account_service.get_by_id(id)
        return jsonify({
            "bank account": {
                "id": bank_account.id,
                "account_number": bank_account.account_number,
                "account_type": bank_account.account_type.value,
                "is_active": bank_account.is_active,
                "balance": bank_account.balance,
            }
        }), 200
    except BankAccountNotFound as e:
        return jsonify({"message": str(e)}), 404

@bank_bp.route('/user/<string:user_id>/bank_account', methods=['GET'])
def get_user_bank_account(user_id:str):
    try:
        bank_account = bank_account_service.get_by_user_id(user_id)
        return jsonify({
            "bank account": {
                "id": bank_account.id,
                "account_number": bank_account.account_number,
                "account_type": bank_account.account_type.value,
                "is_active": bank_account.is_active,
                "balance": bank_account.balance,
                "user_id": bank_account.user_id,
            }
        }), 200
    except BankAccountNotFound as e:
        return jsonify({"message": str(e)}), 404

@bank_bp.route('/bank_account/<string:id>', methods=['PUT'])
def update_bank_account(id:str):
    try:
        bank_account = bank_account_service.update_by_id(id)
        return jsonify({
            "message": "Bank account updated",
            "bank account": {
                "id": bank_account.id,
                "account_number": bank_account.account_number,
                "account_type": bank_account.account_type.value,
                "is_active": bank_account.is_active,
                "balance": bank_account.balance,
                "user_id": bank_account.user_id,
            }
        }), 200
    except BankAccountNotFound as e:
        return jsonify({"message": str(e)}), 404

@bank_bp.route('/bank_account/<string:id>', methods=['DELETE'])
def delete_bank_account(id:str):
    try:
        bank_account_service.delete_by_id(id)
        return jsonify({"message": "Bank account deleted successfully"}), 204
    except BankAccountNotFound as e:
        return jsonify({"message": str(e)}), 404
