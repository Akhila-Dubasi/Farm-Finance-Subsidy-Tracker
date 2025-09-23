from src.dao.transaction_dao import TransactionDAO

class TransactionService:
    @staticmethod
    def add_transaction(farmer_id, transaction_type, amount, date, description=""):
        data = {
            "farmer_id": farmer_id,
            "transaction_type": transaction_type,
            "amount": amount,
            "date": date,
            "description": description
        }
        return TransactionDAO.create(data)

    @staticmethod
    def view_transaction(transaction_id):
        return TransactionDAO.get(transaction_id)

    @staticmethod
    def list_transactions():
        return TransactionDAO.get_all()
