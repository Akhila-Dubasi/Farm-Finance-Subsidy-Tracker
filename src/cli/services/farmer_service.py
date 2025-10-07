# src/cli/services/farmer_service.py
from src.cli.dao.farmer_dao import FarmerDAO

class FarmerService:
    @staticmethod
    def add_farmer(data):
        res = FarmerDAO.insert(data)
        return res.data
    @staticmethod
    def add_farmer(name: str, phone: str):
        farmer_data = {"name": name, "phone": phone}
        return FarmerDAO.insert(farmer_data)
    @staticmethod
    def list_farmers():
        return FarmerDAO.get_all()

    @staticmethod
    def update_farmer(farmer_id, data):
        return FarmerDAO.update(farmer_id, data)

    @staticmethod
    def delete_farmer(farmer_id):
        return FarmerDAO.delete(farmer_id)

    @staticmethod
    def get_farmer(farmer_id):
        return FarmerDAO.get_by_id(farmer_id)
