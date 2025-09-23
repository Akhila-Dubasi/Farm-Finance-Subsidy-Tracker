from src.dao.farmer_dao import FarmerDAO

class FarmerService:
    @staticmethod
    def add_farmer(name, email, phone, address, state, district):
        data = {
            "name": name,
            "email": email,
            "phone": phone,
            "address": address,
            "state": state,
            "district": district
        }
        return FarmerDAO.create(data)

    @staticmethod
    def view_farmer(farmer_id):
        return FarmerDAO.get(farmer_id)

    @staticmethod
    def list_farmers():
        return FarmerDAO.get_all()
