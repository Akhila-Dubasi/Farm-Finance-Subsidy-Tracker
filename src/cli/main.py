# src/cli/main.py
from rich.console import Console
from datetime import datetime

from src.cli.services.farmer_service import FarmerService
from src.cli.services.farm_service import FarmService
from src.cli.services.crop_service import CropService
from src.cli.services.subsidy_service import SubsidyService
from src.cli.services.expense_service import ExpenseService
from src.cli.services.transaction_service import TransactionService

console = Console()

def select_from_list(items, item_name="item"):
    if not items:
        console.print(f"No {item_name}s found.")
        return None
    for i, item in enumerate(items, start=1):
        name = item.get("name") or item.get("scheme") or str(item.get("amount"))
        console.print(f"{i}. {name} ({item.get('id')})")
    while True:
        try:
            choice = int(input(f"Select {item_name} number: "))
            if 1 <= choice <= len(items):
                return items[choice - 1]["id"]
            console.print("Invalid choice. Try again.")
        except ValueError:
            console.print("Please enter a valid number.")

# -------------------- Farmer Menu -------------------- #
def farmers_menu():
    while True:
        console.print("\nFarmer Menu\n1. Add Farmer\n2. List Farmers\n3. Update Farmer\n4. Delete Farmer\n0. Back")
        choice = input("Choice: ")
        if choice == "1":
            name = input("Name: ")
            phone = input("Phone: ")
            res = FarmerService.add_farmer(name, phone)
            console.print(f"Farmer added: {res}")
        elif choice == "2":
            farmers = FarmerService.list_farmers()
            console.print(farmers)
        elif choice == "3":
            farmers = FarmerService.list_farmers()
            farmer_id = select_from_list(farmers, "farmer")
            if farmer_id:
                name = input("New Name: ")
                phone = input("New Phone: ")
                res = FarmerService.update_farmer(farmer_id, name, phone)
                console.print(f"Farmer updated: {res}")
        elif choice == "4":
            farmers = FarmerService.list_farmers()
            farmer_id = select_from_list(farmers, "farmer")
            if farmer_id:
                res = FarmerService.delete_farmer(farmer_id)
                console.print(f"Farmer deleted: {res}")
        elif choice == "0":
            break
        else:
            console.print("Invalid choice.")

# -------------------- Farm Menu -------------------- #
def farms_menu():
    while True:
        console.print("\nFarm Menu\n1. Add Farm\n2. List Farms\n3. Update Farm\n4. Delete Farm\n0. Back")
        choice = input("Choice: ")
        if choice == "1":
            farmers = FarmerService.list_farmers()
            farmer_id = select_from_list(farmers, "farmer")
            if not farmer_id:
                continue
            name = input("Farm Name: ")
            area = input("Area: ")
            location = input("Location: ")
            res = FarmService.add_farm(farmer_id, name, float(area) if area else None, location or None)
            console.print(f"Farm added: {res}")
        elif choice == "2":
            farms = FarmService.list_farms()
            console.print(farms)
        elif choice == "3":
            farms = FarmService.list_farms()
            farm_id = select_from_list(farms, "farm")
            if farm_id:
                name = input("New Name: ")
                area = input("New Area: ")
                location = input("New Location: ")
                res = FarmService.update_farm(farm_id, name or None, float(area) if area else None, location or None)
                console.print(f"Farm updated: {res}")
        elif choice == "4":
            farms = FarmService.list_farms()
            farm_id = select_from_list(farms, "farm")
            if farm_id:
                res = FarmService.delete_farm(farm_id)
                console.print(f"Farm deleted: {res}")
        elif choice == "0":
            break
        else:
            console.print("Invalid choice.")

# -------------------- Crop Menu -------------------- #
def crops_menu():
    while True:
        console.print("\nCrop Menu\n1. Add Crop\n2. List Crops\n3. Update Crop\n4. Delete Crop\n0. Back")
        choice = input("Choice: ")
        if choice == "1":
            farms = FarmService.list_farms()
            farm_id = select_from_list(farms, "farm")
            if not farm_id:
                continue
            name = input("Crop Name: ")
            season = input("Season: ")
            res = CropService.add_crop(farm_id, name, season or None)
            console.print(f"Crop added: {res}")
        elif choice == "2":
            crops = CropService.list_crops()
            console.print(crops)
        elif choice == "3":
            crops = CropService.list_crops()
            crop_id = select_from_list(crops, "crop")
            if crop_id:
                name = input("New Name: ")
                season = input("New Season: ")
                res = CropService.update_crop(crop_id, name or None, season or None)
                console.print(f"Crop updated: {res}")
        elif choice == "4":
            crops = CropService.list_crops()
            crop_id = select_from_list(crops, "crop")
            if crop_id:
                res = CropService.delete_crop(crop_id)
                console.print(f"Crop deleted: {res}")
        elif choice == "0":
            break
        else:
            console.print("Invalid choice.")

# -------------------- Subsidy Menu -------------------- #
def subsidies_menu():
    while True:
        console.print("\nSubsidy Menu\n1. Add Subsidy\n2. List Subsidies\n3. Update Subsidy\n4. Delete Subsidy\n0. Back")
        choice = input("Choice: ")
        if choice == "1":
            farmers = FarmerService.list_farmers()
            farmer_id = select_from_list(farmers, "farmer")
            if not farmer_id:
                continue
            amount = float(input("Amount: "))
            scheme = input("Scheme: ")
            granted_on = input("Granted On (YYYY-MM-DD): ")
            res = SubsidyService.add_subsidy(farmer_id, amount, scheme, granted_on)
            console.print(f"Subsidy added: {res}")
        elif choice == "2":
            subsidies = SubsidyService.list_subsidies()
            console.print(subsidies)
        elif choice == "3":
            subsidies = SubsidyService.list_subsidies()
            subsidy_id = select_from_list(subsidies, "subsidy")
            if subsidy_id:
                amount = input("New Amount: ")
                scheme = input("New Scheme: ")
                granted_on = input("New Granted On (YYYY-MM-DD): ")
                res = SubsidyService.update_subsidy(subsidy_id, float(amount) if amount else None, scheme or None, granted_on or None)
                console.print(f"Subsidy updated: {res}")
        elif choice == "4":
            subsidies = SubsidyService.list_subsidies()
            subsidy_id = select_from_list(subsidies, "subsidy")
            if subsidy_id:
                res = SubsidyService.delete_subsidy(subsidy_id)
                console.print(f"Subsidy deleted: {res}")
        elif choice == "0":
            break
        else:
            console.print("Invalid choice.")

# -------------------- Expense Menu -------------------- #
def expenses_menu():
    while True:
        console.print("\nExpense Menu\n1. Add Expense\n2. List Expenses\n3. Update Expense\n4. Delete Expense\n0. Back")
        choice = input("Choice: ")
        if choice == "1":
            farms = FarmService.list_farms()
            farm_id = select_from_list(farms, "farm")
            if not farm_id:
                continue
            amount = float(input("Amount: "))
            category = input("Category: ")
            spent_on = input("Spent On (YYYY-MM-DD): ")
            note = input("Note: ")
            res = ExpenseService.add_expense(farm_id, amount, category, spent_on, note or None)
            console.print(f"Expense added: {res}")
        elif choice == "2":
            expenses = ExpenseService.list_expenses()
            console.print(expenses)
        elif choice == "3":
            expenses = ExpenseService.list_expenses()
            expense_id = select_from_list(expenses, "expense")
            if expense_id:
                amount = input("New Amount: ")
                category = input("New Category: ")
                spent_on = input("New Spent On (YYYY-MM-DD): ")
                note = input("New Note: ")
                res = ExpenseService.update_expense(expense_id, float(amount) if amount else None, category or None, spent_on or None, note or None)
                console.print(f"Expense updated: {res}")
        elif choice == "4":
            expenses = ExpenseService.list_expenses()
            expense_id = select_from_list(expenses, "expense")
            if expense_id:
                res = ExpenseService.delete_expense(expense_id)
                console.print(f"Expense deleted: {res}")
        elif choice == "0":
            break
        else:
            console.print("Invalid choice.")

# -------------------- Transaction Menu -------------------- #
def transactions_menu():
    while True:
        console.print("\nTransaction Menu\n1. Add Transaction\n2. List Transactions\n3. Update Transaction\n4. Delete Transaction\n0. Back")
        choice = input("Choice: ")
        if choice == "1":
            farmers = FarmerService.list_farmers()
            farmer_id = select_from_list(farmers, "farmer")
            if not farmer_id:
                continue
            amount = float(input("Amount: "))
            tx_type = input("Type (credit/debit): ")
            tx_date = input("Date (YYYY-MM-DD): ")
            note = input("Note: ")
            res = TransactionService.add_transaction(farmer_id, amount, tx_type, tx_date, note or None)
            console.print(f"Transaction added: {res}")
        elif choice == "2":
            transactions = TransactionService.list_transactions()
            console.print(transactions)
        elif choice == "3":
            transactions = TransactionService.list_transactions()
            tx_id = select_from_list(transactions, "transaction")
            if tx_id:
                amount = input("New Amount: ")
                tx_type = input("New Type: ")
                tx_date = input("New Date (YYYY-MM-DD): ")
                note = input("New Note: ")
                res = TransactionService.update_transaction(tx_id, float(amount) if amount else None, tx_type or None, tx_date or None, note or None)
                console.print(f"Transaction updated: {res}")
        elif choice == "4":
            transactions = TransactionService.list_transactions()
            tx_id = select_from_list(transactions, "transaction")
            if tx_id:
                res = TransactionService.delete_transaction(tx_id)
                console.print(f"Transaction deleted: {res}")
        elif choice == "0":
            break
        else:
            console.print("Invalid choice.")

# -------------------- Main Menu -------------------- #
def main():
    while True:
        console.print("\nFarm Finance & Subsidy Tracker\n1. Farmers\n2. Farms\n3. Crops\n4. Subsidies\n5. Expenses\n6. Transactions\n0. Exit")
        choice = input("Select: ")
        if choice == "1":
            farmers_menu()
        elif choice == "2":
            farms_menu()
        elif choice == "3":
            crops_menu()
        elif choice == "4":
            subsidies_menu()
        elif choice == "5":
            expenses_menu()
        elif choice == "6":
            transactions_menu()
        elif choice == "0":
            console.print("Exiting...")
            break
        else:
            console.print("Invalid choice.")

if __name__ == "__main__":
    main()
