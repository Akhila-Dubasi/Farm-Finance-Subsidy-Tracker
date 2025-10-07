# src/cli/dao/subsidy_dao.py
from src.config import supabase

class SubsidyDAO:
    TABLE = "subsidies"

    @staticmethod
    def insert(data):
        return supabase.table(SubsidyDAO.TABLE).insert(data).execute()

    @staticmethod
    def update(subsidy_id, data):
        return supabase.table(SubsidyDAO.TABLE).update(data).eq("id", subsidy_id).execute()

    @staticmethod
    def delete(subsidy_id):
        return supabase.table(SubsidyDAO.TABLE).delete().eq("id", subsidy_id).execute()
    @staticmethod
    def insert(subsidy_data):
        response = supabase.table(SubsidyDAO.TABLE).insert(subsidy_data).execute()
        return response.data
    @staticmethod
    def get_all():
        response = supabase.table(SubsidyDAO.TABLE).select("*").execute()
        return response.data if response.data else []

    @staticmethod
    def get_by_farmer(farmer_id):
        response = supabase.table(SubsidyDAO.TABLE).select("*").eq("farmer_id", farmer_id).execute()
        return response.data if response.data else []

    @staticmethod
    def get_by_id(subsidy_id):
        response = supabase.table(SubsidyDAO.TABLE).select("*").eq("id", subsidy_id).execute()
        return response.data[0] if response.data else None
