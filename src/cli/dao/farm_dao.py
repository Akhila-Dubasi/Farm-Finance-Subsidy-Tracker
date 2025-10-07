# src/cli/dao/farm_dao.py
from src.config import supabase

class FarmDAO:
    TABLE = "farms"

    @staticmethod
    def insert(data):
        return supabase.table(FarmDAO.TABLE).insert(data).execute()
    @staticmethod
    def insert(farm_data):
        response = supabase.table(FarmDAO.TABLE).insert(farm_data).execute()
        return response.data
    @staticmethod
    def update(farm_id, data):
        return supabase.table(FarmDAO.TABLE).update(data).eq("id", farm_id).execute()

    @staticmethod
    def delete(farm_id):
        return supabase.table(FarmDAO.TABLE).delete().eq("id", farm_id).execute()

    @staticmethod
    def get_all():
        response = supabase.table(FarmDAO.TABLE).select("*").execute()
        return response.data if response.data else []

    @staticmethod
    def get_by_id(farm_id):
        response = supabase.table(FarmDAO.TABLE).select("*").eq("id", farm_id).execute()
        return response.data[0] if response.data else None

    @staticmethod
    def get_by_farmer(farmer_id):
        response = supabase.table(FarmDAO.TABLE).select("*").eq("farmer_id", farmer_id).execute()
        return response.data if response.data else []
