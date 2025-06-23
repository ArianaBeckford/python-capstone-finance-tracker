def view_expenses(data): #for each category, print category name and expenses
    for category, expenses in data.items():
        print(f"Category: {category}")
        for description, amount in expenses:
            print(f" - {description}: ${amount}")

def view_summary(data): #for each category, summarize total expenses
    print("Summary: ")
    for category, expenses in data.items():
        total = 0
        for description, amount in expenses:
            total += amount
        print(f"{category}: ${total:.2f}")

def valid_input(text): #checks if description and category input only consists of letters
    for char in text: #if they only contain letters, return true, otherwise return false
        if not char.isalpha():
            return False
    return True

expenses = {}
run = True
print("Welcome to the Personal Finance Tracker")
while run:
    print("What would you like to do?")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. View Summary")
    print("4. Exit")
    choice = input("Choose an option: ")
    if choice == '1':
        try: #raise error for description and category input if inputs are empty or contain non-letters
            description = input("Enter expense description: ")
            if not description:
                raise ValueError("Input is empty, please enter a description.")
            if not valid_input(description):
                raise ValueError("Description must only contain letters.")
            category = input("Enter category: ")
            if not category:
                raise ValueError("Input is empty, please enter a category.")
            if not valid_input(category):
                raise ValueError("Category must only contain letters.")
            try: #raise error for amount if input is not a number or negative
                amount = float(input("Enter amount: "))
            except ValueError:
                raise ValueError("Invalid amount. Please enter a number.")
            if amount < 0:
                raise ValueError("Invalid amount. Please enter a non-negative number.")
        except ValueError as e:
            print(e)
        else:
            if category in expenses: #if category already exists in dictionary, append to its list
                expenses[category].append((description, amount))
            else: #otherwise create new one
                expenses[category] = [(description, amount)]
            print("Expense added successfully.")
    elif choice == '2':
        if expenses:
            view_expenses(expenses)
        else:
            print("Add at least 1 expense to view expenses.")
    elif choice == '3':
        if expenses:
            view_summary(expenses)
        else:
            print("Add at least 1 expense before viewing summary.")
    elif choice == '4':
        print("Goodbye!")
        run = False
    else:
        print("Invalid option. Please choose between 1 and 4.")