# src/cli/dao/expense_dao.py
from src.config import supabase

class ExpenseDAO:
    TABLE = "expenses"

    @staticmethod
    def insert(data):
        return supabase.table(ExpenseDAO.TABLE).insert(data).execute()

    @staticmethod
    def update(expense_id, data):
        return supabase.table(ExpenseDAO.TABLE).update(data).eq("id", expense_id).execute()

    @staticmethod
    def delete(expense_id):
        return supabase.table(ExpenseDAO.TABLE).delete().eq("id", expense_id).execute()

    @staticmethod
    def get_all():
        response = supabase.table(ExpenseDAO.TABLE).select("*").execute()
        return response.data if response.data else []

    @staticmethod
    def get_by_farmer(farmer_id):
        response = supabase.table(ExpenseDAO.TABLE).select("*").eq("farmer_id", farmer_id).execute()
        return response.data if response.data else []

    @staticmethod
    def get_by_id(expense_id):
        response = supabase.table(ExpenseDAO.TABLE).select("*").eq("id", expense_id).execute()
        return response.data[0] if response.data else None
    @staticmethod
    def insert(expense_data):
        response = supabase.table(ExpenseDAO.TABLE).insert(expense_data).execute()
        return response.data