from datetime import datetime
FIL = "data.txt"
Bfile = "budget.txt"
def filex():
    try:
        file = open(FIL, "r")
        file.close()
    except FileNotFoundError:
        file = open(FIL, "w")
        file.close()
def reaex():
    expenses = []
    try:
        file = open(FIL, "r")
        for line in file:
            line = line.strip()
            if line == "":
                continue
            parts = line.split("|")
            if len(parts) == 4:
                expense = {
                    "Date": parts[0],
                    "Category": parts[1],
                    "Amount": parts[2],
                    "Description": parts[3]
                }
                expenses.append(expense)
        file.close()
    except FileNotFoundError:
        filex()
    return expenses
def save(expenses):
    file = open(FIL, "w")
    for ex in expenses:
        file.write(
            ex["Date"] + "|" +
            ex["Category"] + "|" +
            ex["Amount"] + "|" +
            ex["Description"] + "\n"
        )
    file.close()
def adexp():
    print("\n========== ADD EXPENSE ==========")
    date = input(
        "Enter date (DDMMYY) or press Enter for today: "
    )
    if date == "":
        date = datetime.now().strftime("%d-%m-%Y")
    else:
        try:
            datetime.strptime(date, "%d-%m-%Y")
        except ValueError:
            print("Invalid date format.")
            return
    print("\nChoose Category")
    print("1. Food")
    print("2. Travel")
    print("3. Shopping")
    print("4. Education")
    print("5. Entertainment")
    print("6. Bills")
    print("7. Other")
    choice = input("Enter choice: ")
    cat = {
        "1": "Food",
        "2": "Travel",
        "3": "Shopping",
        "4": "Education",
        "5": "Entertainment",
        "6": "Bills",
        "7": "Other"
    }
    if choice not in cat:
        print("Invalid category.")
        return
    cat = cat[choice]
    try:
        amount = float(input("Enter amount: "))
        if amount <= 0:
            print("Amount should be greater than zero.")
            return
    except ValueError:
        print("Please enter a valid amount.")
        return
    description = input("Enter description: ")
    file = open(FIL, "a")
    file.write(
        date + "|" +
        cat + "|" +
        str(amount) + "|" +
        description + "\n"
    )
    file.close()
    print("\nExpense added successfully.")
def shex():
    exs = reaex()
    print("\n========== ALL EXPENSES ==========")
    if len(exs) == 0:
        print("No expenses found.")
        return
    print("-" * 80)
    print(
        f"{'No.':<5}"
        f"{'Date':<15}"
        f"{'Category':<18}"
        f"{'Amount':<12}"
        f"Description"
    )
    print("-" * 80)
    for i in range(len(exs)):
        expense = exs[i]
        print(
            f"{i + 1:<5}"
            f"{expense['Date']:<15}"
            f"{expense['Category']:<18}"
            f"₹{float(expense['Amount']):<11.2f}"
            f"{expense['Description']}"
        )
    print("-" * 80)
def texp():
    expenses = reaex()
    total = 0
    for expense in expenses:
        total = total + float(expense["Amount"])
    print("\n========== TOTAL EXPENSE ==========")
    print("Total money spent: ₹", round(total, 2))
def dexp():
    expenses = reaex()
    date = input("Enter date (DDMMYY): ")
    total = 0
    found = False
    print("\n========== DAILY EXPENSE ==========")
    for expense in expenses:
        if expense["Date"] == date:
            found = True
            amount = float(expense["Amount"])
            total = total + amount
            print(
                expense["Category"],
                "- ₹",
                amount,
                "-",
                expense["Description"]
            )
    if found:
        print("-----------------------------")
        print(
            "Total for",
            date,
            ": ₹",
            round(total, 2)
        )
    else:
        print("No expenses found.")
def sexp():
    expenses = reaex()
    keyword = input(
        "Enter category to search: "
    )
    keyword = keyword.lower()
    found = False
    print("\n========== SEARCH RESULT ==========")
    for expense in expenses:
        category = expense["Category"].lower()
        description = (
            expense["Description"].lower()
        )
        if (
            keyword in category
            or keyword in description
        ):
            found = True
            print(
                expense["Date"],
                "|",
                expense["Category"],
                "| ₹",
                expense["Amount"],
                "|",
                expense["Description"]
            )
    if not found:
        print("No matching expense found.")
def avgexp():
    expenses = reaex()
    if len(expenses) == 0:
        print("No expenses found.")
        return
    total = 0
    for expense in expenses:
        total = total + float(
            expense["Amount"]
        )
    average = total / len(expenses)
    print("\n========== AVERAGE EXPENSE ==========")
    print(
        "Average expense: ₹",
        round(average, 2)
    )
def delexp():
    expenses = reaex()
    if len(expenses) == 0:
        print("No expense available.")
        return
    shex()
    try:
        number = int(
            input(
                "\nEnter expense to delete: "
            )
        )
    except ValueError:
        print("Enter valid number.")
        return
    if number < 1 or number > len(expenses):
        print("Invalid expense.")
        return
    deleted = expenses[number - 1]
    confirm = input(
        "Are you sure? (y/n): "
    )
    if confirm.lower() != "y":
        print("Deletion cancel.")
        return
    expenses.pop(number - 1)
    save(expenses)
    print("\nExpense deleted  successfully.")
    print(
        "Deleted:",
        deleted["Category"],
        "₹",
        deleted["Amount"]
    )
def sebud():
    try:
        budget = float(
            input(
                "Enter monthly budget: "
            )
        )
        if budget <= 0:
            print(
                "Budget should be greater than zero."
            )
            return
        file = open(
            Bfile,
            "w"
        )
        file.write(str(budget))
        file.close()
        print("Monthly budget saved.")
    except ValueError:
        print(
            "enter valid amount."
        )
def tosumm():
    expenses = reaex()
    today = datetime.now().strftime(
        "%d-%m-%Y"
    )
    total = 0
    count = 0
    for expense in expenses:
        if expense["Date"] == today:
            total = total + float(
                expense["Amount"]
            )
            count = count + 1
    print(
        "\n========== TODAY'S SUMMARY =========="
    )
    print("Date:", today)
    print(
        "Number of expenses:",
        count
    )
    print(
        "Total spent: ₹",
        round(total, 2)
    )
def compsum():
    expenses = reaex()
    if len(expenses) == 0:
        print(
            "\nNo expenses avl."
        )
        return
    total = 0
    highest = expenses[0]
    lowest = expenses[0]
    for expense in expenses:
        amount = float(
            expense["Amount"]
        )
        total = total + amount
        if amount > float(
            highest["Amount"]
        ):
            highest = expense
        if amount < float(
            lowest["Amount"]
        ):
            lowest = expense
    print(
        "\n===================================="
    )
    print(
        "           EXPENSE SUMMARY"
    )
    print(
        "===================================="
    )
    print(
        "Number of expenses:",
        len(expenses)
    )
    print(
        "Total spent: ₹",
        round(total, 2)
    )
    print(
        "Average expense: ₹",
        round(
            total / len(expenses),
            2
        )
    )
    print("\nHighest expense:")
    print(
        highest["Category"],
        "- ₹",
        highest["Amount"]
    )
    print("\nLowest expense:")
    print(
        lowest["Category"],
        "- ₹",
        lowest["Amount"]
    )
def manu():
    filex()
    while True:
        print("\n")
        print("=" * 50)
        print(
            "          DAILY EXPENSE TRACKER"
        )
        print("=" * 50)
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Delete Expense")
        print("4. Search Expense")
        print("5. Total Expense")
        print("6. Daily Expense")
        print("7. Average Expense")
        print("8. Set Monthly Budget")
        print("9. Today's Summary")
        print("10. Complete Summary")
        print("11. Exit")
        print("=" * 50)
        choice = input(
            "Enter choice: "
        )
        if choice == "1":
            adexp()
        elif choice == "2":
            shex()
        elif choice == "3":
            delexp()
        elif choice == "4":
            sexp()
        elif choice == "5":
            texp()
        elif choice == "6":
            dexp()
        elif choice == "7":
            avgexp()
        elif choice == "8":
            sebud()
        elif choice == "9":
            tosumm()
        elif choice == "10":
            compsum()
        elif choice == "11":
            print(
                "\nThank you."
                
            )
            break
        else:
            print(
                "\nInvalid choice. "
            )
manu()