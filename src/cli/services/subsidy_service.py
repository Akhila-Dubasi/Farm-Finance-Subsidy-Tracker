# src/cli/services/subsidy_service.py
from src.cli.dao.subsidy_dao import SubsidyDAO

class SubsidyService:
    @staticmethod
    def add_subsidy(data):
        res = SubsidyDAO.insert(data)
        return res.data

    @staticmethod
    def list_subsidies():
        return SubsidyDAO.get_all()

    @staticmethod
    def list_subsidies_by_farmer(farmer_id):
        return SubsidyDAO.get_by_farmer(farmer_id)

    @staticmethod
    def update_subsidy(subsidy_id, data):
        return SubsidyDAO.update(subsidy_id, data)

    @staticmethod
    def delete_subsidy(subsidy_id):
        return SubsidyDAO.delete(subsidy_id)
    @staticmethod
    def add_subsidy(farmer_id, amount, scheme, granted_on):
        subsidy_data = {
            "farmer_id": farmer_id,
            "amount": amount,
            "scheme": scheme,
            "granted_on": str(granted_on)
        }
        return SubsidyDAO.insert(subsidy_data)