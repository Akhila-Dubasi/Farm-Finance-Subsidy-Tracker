# src/cli/services/expense_service.py
from cli.dao.expense_dao import ExpenseDAO

class ExpenseService:
    @staticmethod
    def add_expense(data):
        res = ExpenseDAO.insert(data)
        return res.data

    @staticmethod
    def list_expenses():
        return ExpenseDAO.get_all()

    @staticmethod
    def list_expenses_by_farmer(farmer_id):
        return ExpenseDAO.get_by_farmer(farmer_id)

    @staticmethod
    def update_expense(expense_id, data):
        return ExpenseDAO.update(expense_id, data)

    @staticmethod
    def delete_expense(expense_id):
        return ExpenseDAO.delete(expense_id)
    @staticmethod
    def add_expense(farm_id, amount, category, spent_on, note):
        expense_data = {
            "farm_id": farm_id,
            "amount": amount,
            "category": category,
            "spent_on": str(spent_on),
            "note": note
        }
        return ExpenseDAO.insert(expense_data)