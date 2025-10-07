# src/cli/dao/farmer_dao.py
from src.config import supabase

class FarmerDAO:
    TABLE = "farmers"

    @staticmethod
    def insert(data):
        return supabase.table(FarmerDAO.TABLE).insert(data).execute()

    @staticmethod
    def update(farmer_id, data):
        return supabase.table(FarmerDAO.TABLE).update(data).eq("id", farmer_id).execute()

    @staticmethod
    def delete(farmer_id):
        return supabase.table(FarmerDAO.TABLE).delete().eq("id", farmer_id).execute()

    @staticmethod
    def get_all():
        response = supabase.table(FarmerDAO.TABLE).select("*").execute()
        return response.data if response.data else []

    @staticmethod
    def get_by_id(farmer_id):
        response = supabase.table(FarmerDAO.TABLE).select("*").eq("id", farmer_id).execute()
        return response.data[0] if response.data else None
