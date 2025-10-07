# src/cli/dao/crop_dao.py
from src.config import supabase

class CropDAO:
    TABLE = "crops"

    @staticmethod
    def insert(data):
        return supabase.table(CropDAO.TABLE).insert(data).execute()

    @staticmethod
    def update(crop_id, data):
        return supabase.table(CropDAO.TABLE).update(data).eq("id", crop_id).execute()

    @staticmethod
    def delete(crop_id):
        return supabase.table(CropDAO.TABLE).delete().eq("id", crop_id).execute()

    @staticmethod
    def get_all():
        response = supabase.table(CropDAO.TABLE).select("*").execute()
        return response.data if response.data else []

    @staticmethod
    def get_by_farmer(farmer_id):
        response = supabase.table(CropDAO.TABLE).select("*").eq("farmer_id", farmer_id).execute()
        return response.data if response.data else []
