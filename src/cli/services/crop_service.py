# src/cli/services/crop_service.py
from cli.dao.crop_dao import CropDAO

class CropService:
    @staticmethod
    def add_crop(data):
        res = CropDAO.insert(data)
        return res.data

    @staticmethod
    def list_crops():
        return CropDAO.get_all()

    @staticmethod
    def list_crops_by_farmer(farmer_id):
        return CropDAO.get_by_farmer(farmer_id)

    @staticmethod
    def update_crop(crop_id, data):
        return CropDAO.update(crop_id, data)

    @staticmethod
    def delete_crop(crop_id):
        return CropDAO.delete(crop_id)
    @staticmethod
    def add_crop(farm_id, name, season):
        crop_data = {"farm_id": farm_id, "name": name, "season": season}
        return CropDAO.insert(crop_data)