# src/app.py
import streamlit as st
from datetime import date

# Services imports (adjusted for src folder)
from cli.services.farmer_service import FarmerService
from cli.services.farm_service import FarmService
from cli.services.crop_service import CropService
from cli.services.subsidy_service import SubsidyService
from cli.services.expense_service import ExpenseService
from cli.services.transaction_service import TransactionService

# --- Session State ---
if "farmer_id" not in st.session_state:
    st.session_state.farmer_id = None
if "farmer_name" not in st.session_state:
    st.session_state.farmer_name = None

# --- Login/Signup Page ---
def login_signup():
    st.title("Farm Finance & Subsidy Tracker")
    choice = st.radio("Login or Signup", ["Login", "Signup"])

    if choice == "Signup":
        st.subheader("Signup")
        name = st.text_input("Name")
        phone = st.text_input("Phone")
        if st.button("Signup"):
            farmer = FarmerService.add_farmer(name, phone)
            st.success(f"Farmer created: {farmer[0]['name']}")
    else:
        st.subheader("Login")
        farmers = FarmerService.list_farmers()
        if farmers:
            farmer_dict = {f"{f['name']} ({f['phone']})": f['id'] for f in farmers}
            selected = st.selectbox("Select your account", list(farmer_dict.keys()))
            if st.button("Login"):
                st.session_state.farmer_id = farmer_dict[selected]
                st.session_state.farmer_name = selected
                st.success(f"Logged in as {selected}")
        else:
            st.info("No farmers found. Please signup first.")

# --- Dashboard Page ---
def dashboard():
    st.sidebar.title(f"Welcome, {st.session_state.farmer_name}")

    # --- Fetch all data for stats ---
    farms = FarmService.list_farms_by_farmer(st.session_state.farmer_id)
    crops = CropService.list_crops_by_farmer(st.session_state.farmer_id)
    subsidies = SubsidyService.list_subsidies_by_farmer(st.session_state.farmer_id)
    expenses = ExpenseService.list_expenses_by_farmer(st.session_state.farmer_id)
    transactions = TransactionService.list_transactions_by_farmer(st.session_state.farmer_id)

    # --- Sidebar Statistics ---
    st.sidebar.subheader("Your Stats")
    st.sidebar.metric("Farms", len(farms))
    st.sidebar.metric("Crops", len(crops))
    st.sidebar.metric("Subsidies", len(subsidies))
    st.sidebar.metric("Expenses", len(expenses))
    st.sidebar.metric("Transactions", len(transactions))

    menu = st.sidebar.radio("Menu", ["Farms", "Crops", "Subsidies", "Expenses", "Transactions", "Logout"])

    if menu == "Logout":
        st.session_state.farmer_id = None
        st.session_state.farmer_name = None
        st.experimental_rerun()

    # --- Farms Section ---
    if menu == "Farms":
        st.header("Farms")
        with st.form("Add Farm"):
            name = st.text_input("Farm Name")
            area = st.number_input("Area (acres)", min_value=0.0)
            location = st.text_input("Location")
            submitted = st.form_submit_button("Add Farm")
            if submitted:
                FarmService.add_farm(st.session_state.farmer_id, name, area, location)
                st.success("Farm added!")
                farms = FarmService.list_farms_by_farmer(st.session_state.farmer_id)
        if farms:
            st.table(farms)
        else:
            st.info("No farms added yet.")

    # --- Crops Section ---
    elif menu == "Crops":
        st.header("Crops")
        farm_dict = {f["name"]: f["id"] for f in farms}
        with st.form("Add Crop"):
            farm_selected = st.selectbox("Select Farm", list(farm_dict.keys()))
            name = st.text_input("Crop Name")
            season = st.text_input("Season")
            submitted = st.form_submit_button("Add Crop")
            if submitted:
                CropService.add_crop(farm_dict[farm_selected], name, season)
                st.success("Crop added!")
                crops = CropService.list_crops_by_farmer(st.session_state.farmer_id)
        if crops:
            st.table(crops)
        else:
            st.info("No crops added yet.")

    # --- Subsidies Section ---
    elif menu == "Subsidies":
        st.header("Subsidies")
        with st.form("Add Subsidy"):
            amount = st.number_input("Amount")
            scheme = st.text_input("Scheme")
            granted_on = st.date_input("Granted On", date.today())
            submitted = st.form_submit_button("Add Subsidy")
            if submitted:
                SubsidyService.add_subsidy(st.session_state.farmer_id, amount, scheme, granted_on)
                st.success("Subsidy added!")
                subsidies = SubsidyService.list_subsidies_by_farmer(st.session_state.farmer_id)
        if subsidies:
            st.table(subsidies)
        else:
            st.info("No subsidies added yet.")

    # --- Expenses Section ---
    elif menu == "Expenses":
        st.header("Expenses")
        farm_dict = {f["name"]: f["id"] for f in farms}
        with st.form("Add Expense"):
            farm_selected = st.selectbox("Select Farm", list(farm_dict.keys()))
            amount = st.number_input("Amount")
            category = st.text_input("Category")
            spent_on = st.date_input("Spent On", date.today())
            note = st.text_input("Note")
            submitted = st.form_submit_button("Add Expense")
            if submitted:
                ExpenseService.add_expense(farm_dict[farm_selected], amount, category, spent_on, note)
                st.success("Expense added!")
                expenses = ExpenseService.list_expenses_by_farmer(st.session_state.farmer_id)
        if expenses:
            st.table(expenses)
        else:
            st.info("No expenses added yet.")

    # --- Transactions Section ---
    elif menu == "Transactions":
        st.header("Transactions")
        with st.form("Add Transaction"):
            amount = st.number_input("Amount")
            tx_type = st.text_input("Type (Credit/Debit)")
            tx_date = st.date_input("Transaction Date", date.today())
            note = st.text_input("Note")
            submitted = st.form_submit_button("Add Transaction")
            if submitted:
                TransactionService.add_transaction(st.session_state.farmer_id, amount, tx_type, tx_date, note)
                st.success("Transaction added!")
                transactions = TransactionService.list_transactions_by_farmer(st.session_state.farmer_id)
        if transactions:
            st.table(transactions)
        else:
            st.info("No transactions added yet.")

# --- App Execution ---
def main():
    if st.session_state.farmer_id is None:
        login_signup()
    else:
        dashboard()

if __name__ == "__main__":
    main()
