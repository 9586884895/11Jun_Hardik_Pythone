from Datastore import load_customers
import Datalogic

def banker_menu(customers):
    while True:
        print("\nBanker Menu")
        print("1) Add Customer")
        print("2) View Customer")
        print("3) Search Customer")
        print("4) View All Customers")
        print("5) Total Bank Balance")
        print("6) Back To Main Menu")
        ch = input("Enter Operation You Want To Perform: ").strip()
        if ch == "1": Datalogic.add_customer(customers)
        elif ch == "2": Datalogic.view_customer(customers)
        elif ch == "3": Datalogic.search_customer(customers)
        elif ch == "4": Datalogic.view_all(customers)
        elif ch == "5": Datalogic.total_balance(customers)
        elif ch == "6": break
        else: print("Invalid choice.")

def customer_menu(customers):
    while True:
        print("\nCustomer Menu")
        print("1) Withdraw")
        print("2) Deposit")
        print("3) View Balance")
        print("4) Back To Main Menu")
        ch = input("Enter Operation You Want To Perform: ").strip()
        if ch == "1": Datalogic.withdraw(customers)
        elif ch == "2": Datalogic.deposit(customers)
        elif ch == "3": Datalogic.view_balance(customers)
        elif ch == "4": break
        else: print("Invalid choice.")

def main():
    customers = load_customers()
    while True:
        print("\nWelcome to Python Bank")
        print("1) Banker")
        print("2) Customer")
        print("3) Exit")
        role = input("Select Your Role From Above Menu: ").strip()
        if role == "1": banker_menu(customers)
        elif role == "2": customer_menu(customers)
        elif role == "3":
            print("Thank You Visit Again!.")
            break
        else: print("Invalid selection.")

if __name__ == "__main__":
    main()