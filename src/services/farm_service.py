from src.dao.farm_dao import FarmDAO

class FarmService:
    @staticmethod
    def add_farm(farmer_id, farm_name, location, area_in_acres, soil_type):
        data = {
            "farmer_id": farmer_id,
            "farm_name": farm_name,
            "location": location,
            "area_in_acres": area_in_acres,
            "soil_type": soil_type
        }
        return FarmDAO.create(data)

    @staticmethod
    def view_farm(farm_id):
        return FarmDAO.get(farm_id)

    @staticmethod
    def list_farms():
        return FarmDAO.get_all()
