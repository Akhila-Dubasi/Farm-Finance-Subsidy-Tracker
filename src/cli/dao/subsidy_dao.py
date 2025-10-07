# src/cli/dao/subsidy_dao.py
from src.config import supabase

class SubsidyDAO:
    TABLE = "subsidies"

    @staticmethod
    def insert(data):
        return supabase.table(SubsidyDAO.TABLE).insert(data).execute().data

    @staticmethod
    def list_all():
        res = supabase.table(SubsidyDAO.TABLE).select("*").execute()
        return res.data or []

    @staticmethod
    def update(subsidy_id, data):
        return supabase.table(SubsidyDAO.TABLE).update(data).eq("id", subsidy_id).execute().data

    @staticmethod
    def delete(subsidy_id):
        return supabase.table(SubsidyDAO.TABLE).delete().eq("id", subsidy_id).execute().data
