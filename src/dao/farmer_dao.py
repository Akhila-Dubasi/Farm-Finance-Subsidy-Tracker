from src.config import supabase

class FarmerDAO:
    TABLE = "farmers"

    @staticmethod
    def create(data: dict):
        return supabase.table(FarmerDAO.TABLE).insert(data).execute()

    @staticmethod
    def get(farmer_id: int):
        return supabase.table(FarmerDAO.TABLE).select("*").eq("farmer_id", farmer_id).execute()

    @staticmethod
    def get_all():
        return supabase.table(FarmerDAO.TABLE).select("*").execute()

    @staticmethod
    def update(farmer_id: int, data: dict):
        return supabase.table(FarmerDAO.TABLE).update(data).eq("farmer_id", farmer_id).execute()

    @staticmethod
    def delete(farmer_id: int):
        return supabase.table(FarmerDAO.TABLE).delete().eq("farmer_id", farmer_id).execute()
