# src/cli/services/farm_service.py
from src.cli.dao.farm_dao import FarmDAO

class FarmService:
    @staticmethod
    def add_farm(data):
        res = FarmDAO.insert(data)
        return res.data

    @staticmethod
    def list_farms():
        return FarmDAO.get_all()

    @staticmethod
    def list_farms_by_farmer(farmer_id):
        return FarmDAO.get_by_farmer(farmer_id)

    @staticmethod
    def update_farm(farm_id, data):
        return FarmDAO.update(farm_id, data)

    @staticmethod
    def delete_farm(farm_id):
        return FarmDAO.delete(farm_id)
