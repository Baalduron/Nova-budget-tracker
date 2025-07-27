print("Welcome to the Nova Budget Tracker!")

while True:
    while True:
        try:
            income = float(input("Enter Your Weekly Income: $"))
            if income <= 0:
                print ("⚠ Please enter a positive number.")
                continue
            break
        except ValueError:
            print("⚠ That's not a valid number. Please try again.")
            continue

    print("You Entered: $", income)

    Tithe = income * 0.10
    Savings = income * 0.10
    debt_repayment = income * 0.20
    living_expenses = income * 0.60

    print("\nHere is your 10/10/20/60 Budget Breakdown:")
    print(f"   🟢 Tithe (10%):            ${Tithe:.2f}")
    print(f"   🟢 Savings (10%):          ${Savings:.2f}")
    print(f"   🟡 Debt Repayment (20%)    ${debt_repayment:.2f}")
    print(f"   🔵 Living Expenses (60%):  ${living_expenses:.2f}")

    with open("budget_report.txt", "a") as file:
        file.write(f"Income: ${income:.2f}\n")
        file.write(f"Tithe (10%): ${Tithe:.2f}\n")
        file.write(f"Savings (10%): ${Savings:.2f}\n")
        file.write(f"Debt Repayment (20%): ${debt_repayment:.2f}\n")
        file.write(f"Living Expenses (60%): ${living_expenses:.2f}\n")
        file.write("-" * 40 + "\n")

    repeat = input("\nWould you like to enter another income? (Y/N): ").strip().lower()
    if repeat != 'y':
        print("Goodbye. Stay on mission. 💼")
        break