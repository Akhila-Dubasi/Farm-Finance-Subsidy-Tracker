from src.dao.user_dao import UserDAO

class UserService:
    @staticmethod
    def add_user(farmer_id, username, password_hash, role):
        data = {
            "farmer_id": farmer_id,
            "username": username,
            "password_hash": password_hash,
            "role": role
        }
        return UserDAO.create(data)

    @staticmethod
    def view_user(user_id):
        return UserDAO.get(user_id)

    @staticmethod
    def list_users():
        return UserDAO.get_all()
