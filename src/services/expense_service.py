from src.dao.expense_dao import ExpenseDAO

class ExpenseService:
    @staticmethod
    def add_expense(farm_id, category, amount, date, notes=""):
        data = {
            "farm_id": farm_id,
            "category": category,
            "amount": amount,
            "date": date,
            "notes": notes
        }
        return ExpenseDAO.create(data)

    @staticmethod
    def view_expense(expense_id):
        return ExpenseDAO.get(expense_id)

    @staticmethod
    def list_expenses():
        return ExpenseDAO.get_all()
