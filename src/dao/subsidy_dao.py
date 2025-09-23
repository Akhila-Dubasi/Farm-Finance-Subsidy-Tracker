from src.config import supabase

class SubsidyDAO:
    TABLE = "subsidies"

    @staticmethod
    def create(data: dict):
        return supabase.table(SubsidyDAO.TABLE).insert(data).execute()

    @staticmethod
    def get(subsidy_id: int):
        return supabase.table(SubsidyDAO.TABLE).select("*").eq("subsidy_id", subsidy_id).execute()

    @staticmethod
    def get_all():
        return supabase.table(SubsidyDAO.TABLE).select("*").execute()

    @staticmethod
    def update(subsidy_id: int, data: dict):
        return supabase.table(SubsidyDAO.TABLE).update(data).eq("subsidy_id", subsidy_id).execute()

    @staticmethod
    def delete(subsidy_id: int):
        return supabase.table(SubsidyDAO.TABLE).delete().eq("subsidy_id", subsidy_id).execute()
