# src/cli/dao/transaction_dao.py
from src.config import supabase

class TransactionDAO:
    TABLE = "transactions"

    @staticmethod
    def insert(data):
        return supabase.table(TransactionDAO.TABLE).insert(data).execute()

    @staticmethod
    def update(transaction_id, data):
        return supabase.table(TransactionDAO.TABLE).update(data).eq("id", transaction_id).execute()

    @staticmethod
    def delete(transaction_id):
        return supabase.table(TransactionDAO.TABLE).delete().eq("id", transaction_id).execute()

    @staticmethod
    def get_all():
        response = supabase.table(TransactionDAO.TABLE).select("*").execute()
        return response.data if response.data else []

    @staticmethod
    def get_by_farmer(farmer_id):
        response = supabase.table(TransactionDAO.TABLE).select("*").eq("farmer_id", farmer_id).execute()
        return response.data if response.data else []

    @staticmethod
    def get_by_id(transaction_id):
        response = supabase.table(TransactionDAO.TABLE).select("*").eq("id", transaction_id).execute()
        return response.data[0] if response.data else None
    @staticmethod
    def insert(tx_data):
        response = supabase.table(TransactionDAO.TABLE).insert(tx_data).execute()
        return response.data