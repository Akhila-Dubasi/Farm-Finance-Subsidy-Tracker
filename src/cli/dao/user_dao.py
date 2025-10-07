from src.config import supabase

class UserDAO:
    TABLE = "users"

    @staticmethod
    def create(data: dict):
        return supabase.table(UserDAO.TABLE).insert(data).execute()

    @staticmethod
    def get(user_id: int):
        return supabase.table(UserDAO.TABLE).select("*").eq("user_id", user_id).execute()

    @staticmethod
    def get_all():
        return supabase.table(UserDAO.TABLE).select("*").execute()

    @staticmethod
    def update(user_id: int, data: dict):
        return supabase.table(UserDAO.TABLE).update(data).eq("user_id", user_id).execute()

    @staticmethod
    def delete(user_id: int):
        return supabase.table(UserDAO.TABLE).delete().eq("user_id", user_id).execute()
