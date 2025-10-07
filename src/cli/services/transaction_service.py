# src/cli/services/transaction_service.py
from src.cli.dao.transaction_dao import TransactionDAO

class TransactionService:
    @staticmethod
    def add_transaction(data):
        res = TransactionDAO.insert(data)
        return res.data

    @staticmethod
    def list_transactions():
        return TransactionDAO.get_all()

    @staticmethod
    def list_transactions_by_farmer(farmer_id):
        return TransactionDAO.get_by_farmer(farmer_id)

    @staticmethod
    def update_transaction(transaction_id, data):
        return TransactionDAO.update(transaction_id, data)

    @staticmethod
    def delete_transaction(transaction_id):
        return TransactionDAO.delete(transaction_id)
    @staticmethod
    def add_transaction(farmer_id, amount, tx_type, tx_date, note):
        tx_data = {
            "farmer_id": farmer_id,
            "amount": amount,
            "tx_type": tx_type,
            "tx_date": str(tx_date),
            "note": note
        }
        return TransactionDAO.insert(tx_data)