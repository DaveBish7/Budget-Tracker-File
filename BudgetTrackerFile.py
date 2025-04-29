income = []
expenses = []

print('Welcome to your personal budget tracker')

#Adding incomes
def add_income():
    date_str = input('Enter the date (YYYY-MM-DD): ')
    category = input('Enter the income category: ')
    while True:
        try:
            amount_str = input('Enter the amount: ')
            amount = float(amount_str)
            if amount >= 0:
                break
            else:
                print('Income must be a positive number, you can enter that as an expense')
        except ValueError:
             print("Invalid amount. Please enter a number.")

    income_entry = {'date': date_str, 'category': category, 'amount': amount}
    income.append(income_entry)
    print('Income has been added!')

#Adding expenses
def add_expense():
    date_str = input('Enter the date (YYYY-MM-DD): ')
    category = input('Enter the expense category: ')
    while True:
        try:
            amount_str = input('Enter the amount (negative value): ')
            amount = float(amount_str)
            if amount <= 0:
                break
            else:
                print('Expense must be a negative number, you can enter that as an income')
        except ValueError:
            print("Invalid amount. Please enter a number.")

    expense_entry = {'date': date_str, 'category': category, 'amount': amount}
    expenses.append(expense_entry)
    print('Expense has been added!')

#Viewing transactions
def view_transactions():
    all_transactions = income + expenses
    #Sorted by date in descending order
    all_transactions.sort(key=lambda item: item['date'], reverse=True)

    if not all_transactions:
        print('No transactions were added.')
        return

    print("\n--- All Transactions ---")
    print('{:<10} {:<15} {:<10}'.format('Date', 'Category', 'Amount'))
    print('-' * 35)
    for transaction in all_transactions:
        print('{:<10} {:<15} {:<10}'.format(transaction['date'], transaction['category'], transaction['amount']))
    print("------------------------")

#Calculate Balance
def calculate_balance():
    total_income = sum(item['amount'] for item in income)
    total_expenses = sum(item['amount'] for item in expenses)
    current_balance = total_income + total_expenses
    return current_balance

#User Selection
while True:
    print('\nSelect what you would like to do')
    print('1. Add income')
    print('2. Add expenses')
    print('3. View transactions')
    print('4. View balance')
    print('5. Exit')

    choice = input('Enter your choice (1 - 5): ')

    if choice == '1':
        add_income()
    elif choice == '2':
        add_expense()
    elif choice == '3':
        view_transactions()
    elif choice == '4':
        balance = calculate_balance()
        print(f'Your current balance is {balance}')
    elif choice == '5':
        print("Exiting the budget tracker")
        break
    else:
        print('Invalid choice')