def get_valid_income() -> float:
    while True:
        try:
            income = float(input("enter your weekly income: $"))
            if income <= 0:
                print("⚠ Please enter a positive number.")
                with open("budget_report.txt", "a") as r:
                    r.write("[ERROR] Invalid input: No positive number entered. \n")
                continue
            return income
        except ValueError:
            print("⚠ That is  not a valid number. Please try again.")
            with open("budget_report.txt", "a") as r:
                r.write("[ERROR] Invalid input: Non-numeric characters entered. \n")

print("Welcome to the Nova Budget Tracker!")

from datetime import datetime

def calculate_budget(income):
    """Returns a dictionary with the 10/10/20/60 budget breakdown."""
    return {
        "Tithe": income * 0.10,
        "Savings": income * 0.10,
        "Debt Repayment": income * 0.20,
        "Living Expenses": income * 0.60
    }

while True:
    income = get_valid_income()

    budget = calculate_budget(income)

    print("\nHere is your 10/10/20/60 Budget Breakdown:")
    print(f"   🟢 Tithe (10%):            ${budget['Tithe']:.2f}")
    print(f"   🟢 Savings (10%):          ${budget['Savings']:.2f}")
    print(f"   🟡 Debt Repayment (20%)    ${budget['Debt Repayment']:.2f}")
    print(f"   🔵 Living Expenses (60%):  ${budget['Living Expenses']:.2f}")

    with open("budget_report.txt", "a", encoding="utf-8") as file:
        file.write(f"\n📅 Entry Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        file.write(f"Income: ${income:.2f}\n")
        file.write(f"Tithe (10%): ${budget['Tithe']:.2f}\n")
        file.write(f"Savings (10%): ${budget['Savings']:.2f}\n")
        file.write(f"Debt Repayment (20%): ${budget['Debt Repayment']:.2f}\n")
        file.write(f"Living Expenses (60%): ${budget['Living Expenses']:.2f}\n")
        file.write("-" * 40 + "\n")
    

    repeat = input("\nWould you like to enter another income? (Y/N): ").strip().lower()
    if repeat != 'y':
        print("Goodbye. Stay on mission. 💼")
        break