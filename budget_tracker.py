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

BUDGET_RULES = {
    "Tithe": 0.10,
    "Savings": 0.10,
    "Debt Repayment": 0.20,
    "Living Expenses": 0.60
}

def validate_rules(rules: dict[str, float]) -> None:
    if not rules:
        raise ValueError("No budget rules defined.")
    if any(p < 0 for p in rules.values()):
        raise ValueError("Percentages nust be non-negative.")
    total = round(sum(rules.values()), 6)
    if total != 1.0:
        raise ValueError(f"Percentages must sum to 1.0; got {total}.")

def calculate_budget(income: float, rules: dict[str, float] = BUDGET_RULES) -> dict[str, float]:
    validate_rules(rules)
    return {name: round(income * pct, 2) for name, pct in rules.items()}

def _self_test():
    # Happy path
    rules = {"A": 0.5, "B": 0.5}
    out = calculate_budget(100.0, rules)
    assert out["A"] == 50.00 and out["B"] == 50.00

    # Sum not 1.0
    try:
        validate_rules({"A": 0.3, "B": 0.3})
        raise AssertionError("Expected ValueError for bad sum")
    except ValueError:
        pass

    # Negative percentage
    try:
        validate_rules({"A": -0.1, "B": 1.1})
        raise AssertionError("Expected ValueError for negative pct")
    except ValueError:
        pass

    print("✅ _self_test passed")

while True:
    validate_rules(BUDGET_RULES)
    income = get_valid_income()

    budget = calculate_budget(income, BUDGET_RULES)

    print("\nHere is your 10/10/20/60 Budget Breakdown:")
    for name, amount in budget.items():
        print (f"• {name:16} ${amount:>8.2f}")

    with open("budget_report.txt", "a", encoding="utf-8") as file:
        file.write(f"\n📅 Entry Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        file.write(f"Income: ${income:.2f}\n")        
        for name, amount in budget.items():
            file.write(f"• {name:16} ${amount:>8.2f}\n")
        file.write("-" * 40 + "\n")
    

    repeat = input("\nWould you like to enter another income? (Y/N): ").strip().lower()
    if repeat != 'y':
        print("Goodbye. Stay on mission. 💼")
        break
_self_test()