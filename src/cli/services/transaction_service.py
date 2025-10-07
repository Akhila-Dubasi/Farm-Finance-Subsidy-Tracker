# src/cli/services/transaction_service.py
from src.cli.dao.transaction_dao import TransactionDAO

class TransactionService:

    @staticmethod
    def add_transaction(farmer_id, amount, tx_type, tx_date, note=None):
        data = {"farmer_id": farmer_id, "amount": amount, "tx_type": tx_type, "tx_date": tx_date, "note": note}
        return TransactionDAO.insert(data)

    @staticmethod
    def list_transactions():
        return TransactionDAO.list_all()

    @staticmethod
    def update_transaction(tx_id, amount=None, tx_type=None, tx_date=None, note=None):
        data = {}
        if amount:
            data["amount"] = amount
        if tx_type:
            data["tx_type"] = tx_type
        if tx_date:
            data["tx_date"] = tx_date
        if note:
            data["note"] = note
        return TransactionDAO.update(tx_id, data)

    @staticmethod
    def delete_transaction(tx_id):
        return TransactionDAO.delete(tx_id)
    @staticmethod
    def list_transactions_by_farmer(farmer_id):
        transactions = TransactionDAO.get_all()
        return [t for t in transactions if t['farmer_id'] == farmer_id]
