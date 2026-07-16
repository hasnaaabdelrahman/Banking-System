from flask import Flask, request , Blueprint, jsonify

from services.transaction_services import TransactionService
from repositories.transaction_repository import TransactionRepository
from database.db import session

transaction_repository = TransactionRepository(session)
transaction_service = TransactionService(transaction_repository)

transaction_bp = Blueprint('transaction', __name__)

@transaction_bp.route('/transaction', methods=['POST'])
def create_transaction():
    data = request.json
    transaction_data = transaction_service.create_transaction(data)
    return jsonify({
        "message": "Transaction created successfully",
        "transaction": {
            "id": transaction_data.id,
            "account_id": transaction_data.account_id,
            "amount": transaction_data.amount,
            "date": transaction_data.date,
            "transaction_type": transaction_data.transaction_type
        }
    }), 201

@transaction_bp.route('/transaction/<string:id>', methods=['GET'])
def get_transaction(id:str):
    transaction_data = transaction_service.get_transaction_by_id(id)
    if not transaction_data:
        return jsonify({"message": "Transaction not found"}), 404
    return jsonify({
        "id": transaction_data.id,
        "account_id": transaction_data.account_id,
        "amount": transaction_data.amount,
        "date": transaction_data.date,
        "transaction_type": transaction_data.transaction_type
    }), 200

@transaction_bp.route('/transactions', methods=['GET'])
def get_all_transactions():
    transactions = transaction_service.get_all_transactions()
    return jsonify({
        "transactions":[ {
                "id": transaction_data.id,
                "account_id": transaction_data.account_id,
                "amount": transaction_data.amount,
                "date": transaction_data.date,
                "transaction_type": transaction_data.transaction_type
        }] for transaction_data in transactions
    }), 200

@transaction_bp.route('/transaction/<string:id>', methods=['GET'])
def get_transaction_by_account_id(id:str):
    transactions = transaction_service.get_transaction_by_account_id(id)
    if not transactions:
        return jsonify({"message": "Transaction not found"}), 404

    return jsonify({
        "transaction": [{
        "id": transaction_data.id,
        "account_id": transaction_data.account_id,
        "amount": transaction_data.amount,
        "date": transaction_data.date,
        "transaction_type": transaction_data.transaction_type
        }] for transaction_data in transactions
    }), 200

@transaction_bp.route('/transaction', methods=['PUT'])
def update_transaction():
    data = request.json
    transaction_data = transaction_service.update_transaction(data)
    if not transaction_data:
        return jsonify({"message": "Transaction not found"}), 404
    return jsonify({
        "message": "Transaction updated successfully",
        "transaction": {
            "id": transaction_data.id,
            "account_id": transaction_data.account_id,
            "amount": transaction_data.amount,
            "date": transaction_data.date,
            "transaction_type": transaction_data.transaction_type
        }
    }), 200

@transaction_bp.route('/transaction', methods=['DELETE'])
def delete_transaction():
    data = request.json
    transaction_data = transaction_service.delete_transaction(data)
    if not transaction_data:
        return jsonify({"message": "Transaction not found"}), 404
    return jsonify({"message": "Transaction deleted successfully"}) , 204