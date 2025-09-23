from src.dao.crop_dao import CropDAO

class CropService:
    @staticmethod
    def add_crop(farm_id, crop_name, sowing_date, harvest_date, quantity, unit):
        data = {
            "farm_id": farm_id,
            "crop_name": crop_name,
            "sowing_date": sowing_date,
            "harvest_date": harvest_date,
            "quantity": quantity,
            "unit": unit
        }
        return CropDAO.create(data)

    @staticmethod
    def view_crop(crop_id):
        return CropDAO.get(crop_id)

    @staticmethod
    def list_crops():
        return CropDAO.get_all()
