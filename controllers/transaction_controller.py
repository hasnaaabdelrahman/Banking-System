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
    transaction = transaction_service.create_transaction(data)
    return jsonify(transaction), 201

@transaction_bp.route('/transaction/<str:id>', methods=['GET'])
def get_transaction(id:str):
    transaction = transaction_service.get_transaction_by_id(id)
    return jsonify(transaction), 200

@transaction_bp.route('/transactions', methods=['GET'])
def get_all_transactions():
    transactions = transaction_service.get_all_transactions()
    return jsonify(transactions), 200

@transaction_bp.route('/transaction/<str:id>', methods=['GET'])
def get_transaction_by_account_id(id:str):
    transaction = transaction_service.get_transaction_by_account_id(id)
    return jsonify(transaction), 200

@transaction_bp.route('/transaction', methods=['PUT'])
def update_transaction():
    data = request.json
    transaction = transaction_service.update_transaction(data)
    return jsonify(transaction), 200

@transaction_bp.route('/transaction', methods=['DELETE'])
def delete_transaction():
    data = request.json
    transaction_service.delete_transaction(data)
    return '' , 204