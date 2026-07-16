from flask import Flask, request , Blueprint, jsonify

from exceptions.transaction_exceptions import TransactionNotFound
from schemas.transaction_schema import TransactionSchema
from services.transaction_services import TransactionService
from repositories.transaction_repository import TransactionRepository
from database.db import session

transaction_repository = TransactionRepository(session)
transaction_service = TransactionService(transaction_repository)

transaction_bp = Blueprint('transaction', __name__)

@transaction_bp.route('/transaction', methods=['POST'])
def create_transaction():
    data = request.json
    transaction_data = TransactionSchema(**data)
    transaction = transaction_service.create_transaction(transaction_data)
    return jsonify({
        "message": "Transaction created successfully",
        "transaction": {
            "id": transaction.id,
            "account_id": transaction.account_id,
            "amount": transaction.amount,
            "date": transaction.date,
            "transaction_type": transaction.transaction_type.value
        }
    }), 201

@transaction_bp.route('/transaction/<string:id>', methods=['GET'])
def get_transaction(id:str):
    try:
        transaction_data = transaction_service.get_transaction_by_id(id)
        return jsonify({
            "id": transaction_data.id,
            "account_id": transaction_data.account_id,
            "amount": transaction_data.amount,
            "date": transaction_data.date,
            "transaction_type": transaction_data.transaction_type.value
        }), 200
    except TransactionNotFound as e:
        return jsonify({"message": str(e)}), 404

@transaction_bp.route('/transactions', methods=['GET'])
def get_all_transactions():
    transactions = transaction_service.get_all_transactions()
    return jsonify({
        "transactions":[ {
                "id": transaction_data.id,
                "account_id": transaction_data.account_id,
                "amount": transaction_data.amount,
                "date": transaction_data.date,
                "transaction_type": transaction_data.transaction_type.value
        }] for transaction_data in transactions
    }), 200

@transaction_bp.route('/transaction/<string:id>', methods=['GET'])
def get_transaction_by_account_id(id:str):
    try:
        transactions = transaction_service.get_transaction_by_account_id(id)
        return jsonify({
            "transaction": [{
            "id": transaction_data.id,
            "account_id": transaction_data.account_id,
            "amount": transaction_data.amount,
            "date": transaction_data.date,
            "transaction_type": transaction_data.transaction_type.value
            }] for transaction_data in transactions
        }), 200
    except TransactionNotFound as e:
        return jsonify({"message": str(e)}), 404


@transaction_bp.route('/transaction', methods=['PUT'])
def update_transaction():
    try:
        data = request.json
        transaction_data = transaction_service.update_transaction(**data)
        return jsonify({
            "message": "Transaction updated successfully",
            "transaction": {
                "id": transaction_data.id,
                "account_id": transaction_data.account_id,
                "amount": transaction_data.amount,
                "date": transaction_data.date,
                "transaction_type": transaction_data.transaction_type.value
            }
        }), 200
    except TransactionNotFound as e:
        return jsonify({"message": str(e)}), 404

@transaction_bp.route('/transaction', methods=['DELETE'])
def delete_transaction():
    try:
        data = request.json
        transaction_service.delete_transaction(**data)
        return jsonify({"message": "Transaction deleted successfully"}) , 204
    except TransactionNotFound as e:
        return jsonify({"message": str(e)}), 404