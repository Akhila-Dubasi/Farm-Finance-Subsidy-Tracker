from src.services.farmer_service import FarmerService
from src.services.farm_service import FarmService
from src.services.crop_service import CropService
from src.services.expense_service import ExpenseService
from src.services.subsidy_service import SubsidyService
from src.services.transaction_service import TransactionService
from src.services.user_service import UserService
def main():
    print("Farm Finance & Subsidy Tracker")

    while True:
        print("\nMenu:")
        print("1.Add Farmer   2.List Farmers")
        print("3.Add Farm     4.List Farms")
        print("5.Add Crop     6.List Crops")
        print("7.Add Expense  8.List Expenses")
        print("9.Add Subsidy  10.List Subsidies")
        print("11.Add Transaction  12.List Transactions")
        print("13.Add User    14.List Users")
        print("15.Exit")

        choice = input("Enter choice: ")
        # Farmer
        if choice == "1":
            name = input("Name: ")
            email = input("Email: ")
            phone = input("Phone: ")
            address = input("Address: ")
            state = input("State: ")
            district = input("District: ")
            print(FarmerService.add_farmer(name, email, phone, address, state, district))
        elif choice == "2":
            print(FarmerService.list_farmers())
        #Farm 
        elif choice == "3":
            farmer_id = int(input("Farmer ID: "))
            farm_name = input("Farm Name: ")
            location = input("Location: ")
            area = float(input("Area in Acres: "))
            soil_type = input("Soil Type: ")
            print(FarmService.add_farm(farmer_id, farm_name, location, area, soil_type))
        elif choice == "4":
            print(FarmService.list_farms())
        # Crop 
        elif choice == "5":
            farm_id = int(input("Farm ID: "))
            crop_name = input("Crop Name: ")
            sowing_date = input("Sowing Date (YYYY-MM-DD): ")
            harvest_date = input("Harvest Date (YYYY-MM-DD): ")
            quantity = float(input("Quantity: "))
            unit = input("Unit (kg/lbs/etc): ")
            print(CropService.add_crop(farm_id, crop_name, sowing_date, harvest_date, quantity, unit))
        elif choice == "6":
            print(CropService.list_crops())
        #Expense
        elif choice == "7":
            farm_id = int(input("Farm ID: "))
            category = input("Category: ")
            amount = float(input("Amount: "))
            date = input("Date (YYYY-MM-DD): ")
            notes = input("Notes (optional): ")
            print(ExpenseService.add_expense(farm_id, category, amount, date, notes))
        elif choice == "8":
            print(ExpenseService.list_expenses())
        #Subsidy
        elif choice == "9":
            farmer_id = int(input("Farmer ID: "))
            subsidy_name = input("Subsidy Name: ")
            amount = float(input("Amount: "))
            date_received = input("Date Received (YYYY-MM-DD): ")
            status = input("Status (Pending/Approved): ")
            notes = input("Notes (optional): ")
            print(SubsidyService.add_subsidy(farmer_id, subsidy_name, amount, date_received, status, notes))
        elif choice == "10":
            print(SubsidyService.list_subsidies())
        # Transaction
        elif choice == "11":
            farmer_id = int(input("Farmer ID: "))
            transaction_type = input("Transaction Type (Income/Expense): ")
            amount = float(input("Amount: "))
            date = input("Date (YYYY-MM-DD): ")
            description = input("Description (optional): ")
            print(TransactionService.add_transaction(farmer_id, transaction_type, amount, date, description))
        elif choice == "12":
            print(TransactionService.list_transactions())
        #User
        elif choice == "13":
            farmer_id = int(input("Farmer ID (optional, 0 if none): "))
            username = input("Username: ")
            password_hash = input("Password Hash: ")
            role = input("Role (Admin/Farmer/User): ")
            print(UserService.add_user(farmer_id, username, password_hash, role))
        elif choice == "14":
            print(UserService.list_users())
        elif choice == "15":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")
if __name__ == "__main__":
    main()
