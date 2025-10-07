# src/cli/services/subsidy_service.py
from src.cli.dao.subsidy_dao import SubsidyDAO

class SubsidyService:

    @staticmethod
    def add_subsidy(farmer_id, amount, scheme, granted_on):
        data = {"farmer_id": farmer_id, "amount": amount, "scheme": scheme, "granted_on": granted_on}
        return SubsidyDAO.insert(data)

    @staticmethod
    def list_subsidies():
        return SubsidyDAO.list_all()

    @staticmethod
    def update_subsidy(subsidy_id, amount=None, scheme=None, granted_on=None):
        data = {}
        if amount:
            data["amount"] = amount
        if scheme:
            data["scheme"] = scheme
        if granted_on:
            data["granted_on"] = granted_on
        return SubsidyDAO.update(subsidy_id, data)

    @staticmethod
    def delete_subsidy(subsidy_id):
        return SubsidyDAO.delete(subsidy_id)
    @staticmethod
    def list_subsidies_by_farmer(farmer_id):
        subsidies = SubsidyDAO.get_all()
        return [s for s in subsidies if s['farmer_id'] == farmer_id]