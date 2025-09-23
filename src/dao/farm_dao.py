from src.config import supabase

class FarmDAO:
    TABLE = "farms"

    @staticmethod
    def create(data: dict):
        return supabase.table(FarmDAO.TABLE).insert(data).execute()

    @staticmethod
    def get(farm_id: int):
        return supabase.table(FarmDAO.TABLE).select("*").eq("farm_id", farm_id).execute()

    @staticmethod
    def get_all():
        return supabase.table(FarmDAO.TABLE).select("*").execute()

    @staticmethod
    def update(farm_id: int, data: dict):
        return supabase.table(FarmDAO.TABLE).update(data).eq("farm_id", farm_id).execute()

    @staticmethod
    def delete(farm_id: int):
        return supabase.table(FarmDAO.TABLE).delete().eq("farm_id", farm_id).execute()
