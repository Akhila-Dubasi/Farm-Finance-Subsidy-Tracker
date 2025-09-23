from src.dao.subsidy_dao import SubsidyDAO

class SubsidyService:
    @staticmethod
    def add_subsidy(farmer_id, subsidy_name, amount, date_received, status="Pending", notes=""):
        data = {
            "farmer_id": farmer_id,
            "subsidy_name": subsidy_name,
            "amount": amount,
            "date_received": date_received,
            "status": status,
            "notes": notes
        }
        return SubsidyDAO.create(data)

    @staticmethod
    def view_subsidy(subsidy_id):
        return SubsidyDAO.get(subsidy_id)

    @staticmethod
    def list_subsidies():
        return SubsidyDAO.get_all()
