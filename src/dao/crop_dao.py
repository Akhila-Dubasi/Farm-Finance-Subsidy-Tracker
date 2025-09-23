from src.config import supabase
class CropDAO:
    TABLE="crops"
    @staticmethod
    def create(data:dict):
        return supabase.table(CropDAO.TABLE).insert(data).execute()
    @staticmethod
    def get(crop_id:int):
        return supabase.table(CropDAO.TABLE).select("*").eq("crop_id",crop_id).execute()
    @staticmethod
    def get_all():
        return supabase.table(CropDAO.TABLE).select("*").execute()
    @staticmethod
    def update(crop_id:int,data:dict):
        return supabase.table(CropDAO.TABLE).update(data).eq("crop_id",crop_id).execute()
    @staticmethod
    def delete(crop_id:int):
        return supabase.table(CropDAO.TABLE).delete().eq("crop_id",crop_id).execute()
