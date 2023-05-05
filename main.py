import sys
from expense import Expense

def add_expense(data_file):
    description = input("Enter expense description: ")
    amount = float(input("Enter expense amount: "))
    category = input("Enter expense category: ")
    date = input("Enter expense date (YYYY-MM-DD): ")
    expense = Expense(description, amount, category, date)

    with open(data_file, 'a') as file:
        file.write(f"{expense}\n")

def view_expenses(data_file):
    with open(data_file, 'r') as file:
        for line in file:
            print(line.strip())

def remove_expense(data_file, expense_id):
    with open(data_file, 'r') as file:
        expenses = file.readlines()

    if 0 < expense_id <= len(expenses):
        del expenses[expense_id - 1]
        with open(data_file, 'w') as file:
            file.writelines(expenses)
    else:
        print("Invalid expense ID.")

def main():
    data_file = 'data.txt'
    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Remove Expense")
        print("4. Quit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            add_expense(data_file)
        elif choice == 2:
            view_expenses(data_file)
        elif choice == 3:
            expense_id = int(input("Enter expense ID to remove: "))
            remove_expense(data_file, expense_id)
        elif choice == 4:
            sys.exit()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
