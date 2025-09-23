from src.config import supabase

class TransactionDAO:
    TABLE = "transactions"

    @staticmethod
    def create(data: dict):
        return supabase.table(TransactionDAO.TABLE).insert(data).execute()

    @staticmethod
    def get(transaction_id: int):
        return supabase.table(TransactionDAO.TABLE).select("*").eq("transaction_id", transaction_id).execute()

    @staticmethod
    def get_all():
        return supabase.table(TransactionDAO.TABLE).select("*").execute()

    @staticmethod
    def update(transaction_id: int, data: dict):
        return supabase.table(TransactionDAO.TABLE).update(data).eq("transaction_id", transaction_id).execute()

    @staticmethod
    def delete(transaction_id: int):
        return supabase.table(TransactionDAO.TABLE).delete().eq("transaction_id", transaction_id).execute()
