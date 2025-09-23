from src.config import supabase

class ExpenseDAO:
    TABLE = "expenses"

    @staticmethod
    def create(data: dict):
        return supabase.table(ExpenseDAO.TABLE).insert(data).execute()

    @staticmethod
    def get(expense_id: int):
        return supabase.table(ExpenseDAO.TABLE).select("*").eq("expense_id", expense_id).execute()

    @staticmethod
    def get_all():
        return supabase.table(ExpenseDAO.TABLE).select("*").execute()

    @staticmethod
    def update(expense_id: int, data: dict):
        return supabase.table(ExpenseDAO.TABLE).update(data).eq("expense_id", expense_id).execute()

    @staticmethod
    def delete(expense_id: int):
        return supabase.table(ExpenseDAO.TABLE).delete().eq("expense_id", expense_id).execute()
