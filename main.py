def num(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Enter a valid number.")


def create_profile():
    p = {"incomes": [], "expenses": []}
    for i in range(int(num("How many income streams? "))):
        p["incomes"].append(num(f"Monthly income {i+1} (Rs): "))
    for i in range(int(num("How many fixed expenses? "))):
        amount = num(f"Monthly amount of expense {i+1} (Rs): ")
        inflation = num("Yearly inflation %: ")
        p["expenses"].append((amount, inflation))
    p["savings"] = num("Current savings (Rs): ")
    p["rate"] = num("Savings interest % per year: ")
    return p


def simulate(p):
    if not p:
        print("Create or load a profile first.")
        return
    balance, income = p["savings"], sum(p["incomes"])
    print(f"{'Year':<5}|{'Income/mo':>10}|{'Expense/mo':>11}|{'Balance':>14}")
    for month in range(1, 61):
        year = (month - 1) // 12
        expense = sum(a * (1 + r / 100) ** year for a, r in p["expenses"])
        balance += balance * p["rate"] / 1200 + income - expense
        if month % 12 == 0:
            print(f"{month // 12:<5}|{income:>10.0f}|{expense:>11.0f}|{balance:>14,.2f}")
    print(f"Final balance after 5 years: Rs {balance:,.2f}")


profile = None
while True:
    print("\n1. Create profile\n2. Sample profile\n3. Run projection\n4. Exit")
    choice = input("Choose: ")
    if choice == "1":
        profile = create_profile()
    elif choice == "2":
        profile = {"incomes": [60000], "expenses": [(25000, 6)],
                   "savings": 199781, "rate": 6.5}
    elif choice == "3":
        simulate(profile)
    elif choice == "4":
        break
    else:
        print("Invalid choice.")
