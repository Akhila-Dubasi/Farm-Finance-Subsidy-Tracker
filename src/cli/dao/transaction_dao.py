# src/cli/dao/transaction_dao.py
from src.config import supabase

class TransactionDAO:
    TABLE = "transactions"

    @staticmethod
    def insert(data):
        return supabase.table(TransactionDAO.TABLE).insert(data).execute().data

    @staticmethod
    def list_all():
        res = supabase.table(TransactionDAO.TABLE).select("*").execute()
        return res.data or []

    @staticmethod
    def update(tx_id, data):
        return supabase.table(TransactionDAO.TABLE).update(data).eq("id", tx_id).execute().data

    @staticmethod
    def delete(tx_id):
        return supabase.table(TransactionDAO.TABLE).delete().eq("id", tx_id).execute().data
