# src/cli/services/expense_service.py
from src.cli.dao.expense_dao import ExpenseDAO
from src.cli.dao.farm_dao import FarmDAO
class ExpenseService:

    @staticmethod
    def add_expense(farm_id, amount, category, spent_on, note=None):
        data = {"farm_id": farm_id, "amount": amount, "category": category, "spent_on": spent_on, "note": note}
        return ExpenseDAO.insert(data)

    @staticmethod
    def list_expenses():
        return ExpenseDAO.list_all()

    @staticmethod
    def update_expense(expense_id, amount=None, category=None, spent_on=None, note=None):
        data = {}
        if amount:
            data["amount"] = amount
        if category:
            data["category"] = category
        if spent_on:
            data["spent_on"] = spent_on
        if note:
            data["note"] = note
        return ExpenseDAO.update(expense_id, data)

    @staticmethod
    def delete_expense(expense_id):
        return ExpenseDAO.delete(expense_id)
    @staticmethod
    def list_expenses_by_farmer(farmer_id):
        farms = FarmDAO.get_all()
        farmer_farms = [f['id'] for f in farms if f['farmer_id'] == farmer_id]
        expenses = ExpenseDAO.get_all()
        return [e for e in expenses if e['farm_id'] in farmer_farms]
