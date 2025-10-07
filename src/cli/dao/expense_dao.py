# src/cli/dao/expense_dao.py
from src.config import supabase

class ExpenseDAO:
    TABLE = "expenses"

    @staticmethod
    def insert(data):
        return supabase.table(ExpenseDAO.TABLE).insert(data).execute().data

    @staticmethod
    def list_all():
        res = supabase.table(ExpenseDAO.TABLE).select("*").execute()
        return res.data or []

    @staticmethod
    def update(expense_id, data):
        return supabase.table(ExpenseDAO.TABLE).update(data).eq("id", expense_id).execute().data

    @staticmethod
    def delete(expense_id):
        return supabase.table(ExpenseDAO.TABLE).delete().eq("id", expense_id).execute().data
