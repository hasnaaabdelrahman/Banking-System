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
    return jsonify({
        "message": "Bank account created",
        "bank account": {
            "id": bank_account.id,
            "account_number": bank_account.account_number,
            "account_type": bank_account.account_type,
            "is_active": bank_account.is_active,
            "balance": bank_account.balance,
            "user_id": bank_account.user_id,
        }
    }), 201

@bank_bp.route('/bank_account/<string:id>', methods=['GET'])
def get_bank_account(id:str):
    bank_account = bank_account_service.get_by_id(id)
    if not bank_account:
        return jsonify({"message": "Bank account not found"}), 404
    return jsonify({
        "bank account": {
            "id": bank_account.id,
            "account_number": bank_account.account_number,
            "account_type": bank_account.account_type,
            "is_active": bank_account.is_active,
            "balance": bank_account.balance,
        }
    }), 200

@bank_bp.route('/user/<string:user_id>/bank_account', methods=['GET'])
def get_user_bank_account(user_id:str):
    bank_account = bank_account_service.get_by_user_id(user_id)
    if not bank_account:
        return jsonify({"message": "Bank account not found"}), 404
    return jsonify({
        "bank account": {
            "account_number": bank_account.account_number,
            "account_type": bank_account.account_type,
            "is_active": bank_account.is_active,
            "balance": bank_account.balance,
            "user_id": bank_account.user_id,
        }
    }), 200

@bank_bp.route('/bank_account/<string:id>', methods=['PUT'])
def update_bank_account(id:str):
    bank_account = bank_account_service.update_by_id(id)
    if not bank_account:
        return jsonify({"message": "Bank account not found"}), 404
    return jsonify({
        "message": "Bank account updated",
        "bank account": {
            "id": bank_account.id,
            "account_number": bank_account.account_number,
            "account_type": bank_account.account_type,
            "is_active": bank_account.is_active,
            "balance": bank_account.balance,
            "user_id": bank_account.user_id,
        }
    }), 200

@bank_bp.route('/bank_account/<string:id>', methods=['DELETE'])
def delete_bank_account(id:str):
    bank_data= bank_account_service.delete_by_id(id)
    if not bank_data:
        return jsonify({"message": "Bank account not found"}), 404
    return jsonify({"message": "Bank account deleted successfully"}), 204
