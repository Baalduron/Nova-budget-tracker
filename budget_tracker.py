def get_valid_income() -> float:
    while True:
        try:
            income = float(input("enter your weekly income: $"))
            if income <= 0:
                print("⚠ Please enter a positive number.")
                with REPORT_PATH.open("a", encoding="utf-8") as f:
                    f.write("[ERROR] Invalid input: No positve number entered.\n")
                continue
            return income
        except ValueError:
            print("⚠ That is not a valid number. Please try again.")
            with REPORT_PATH.open("a", encoding="utf-8") as f:
                f.write("[ERROR] Invalid input: Non-numeric characters entered.\n")

def main_menu():
    while True:
        print("\n--- Nova Budget Tracker ---")
        print("1. Enter New Income")
        print("2. Review Past Reports")
        print("3. Exit")

        choice = input("Select an Option (1-3): ")

        if choice == "1":
            run_budget_session()
        elif choice == "2":
            review_reports()
        elif choice == "3":
            print("Goodbye. Stay on Mission. 💼")
            exit()
        else:
            print("⚠ Invalid Choice. Please enter 1, 2, or 3.")
           
def review_reports():
    """Print the last 20 lines of budget report file, if present."""
    path = REPORT_PATH

    try:
        with open(path, "r", encoding="utf-8") as f:
            lines = f.readlines()
        if not lines:
            print("\n(No Past Reports Found.)")
            return
        print("\n--- Recent Report Excerpts (last 20 lines) ---")
        for line in lines[-20:]:
            print(line.rstrip("\n"))
        print("--- end ---")
    except FileNotFoundError:
        print("\n(No Past Reports Found - file does not exist yet.)")

from datetime import datetime
from pathlib import Path

REPORT_PATH = Path(__file__).with_name("budget_report.txt")
print(f"[log file] {REPORT_PATH.resolve()}")
with REPORT_PATH.open("a", encoding="utf-8") as f:
    f.write("[BOOT] App started OK\n")

print("Welcome to the Nova Budget Tracker!")

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
        raise ValueError("Percentages must be non-negative.")
    total = round(sum(rules.values()), 6)
    if total != 1.0:
        raise ValueError(f"Percentages must sum to 1.0; got {total}.")

def calculate_budget(income: float, rules: dict[str, float] = BUDGET_RULES) -> dict[str, float]:
    validate_rules(rules)
    return {catagory: round(income * pct, 2) for catagory, pct in rules.items()}

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

def run_budget_session():
    """Handle one budget entry: validation, input, calculation, print, log."""
    validate_rules(BUDGET_RULES)
    income = get_valid_income()
    budget = calculate_budget(income, BUDGET_RULES)

    print("\nHere is your 10/10/20/60 Budget Breakdown:")
    for category, amount in budget.items():
            print(f"• {category:16} ${amount:8.2f}")

    with open(REPORT_PATH, "a", encoding="utf-8") as file:
        file.write(f"\n📅 Entry Date: {datetime.now() .strftime('%Y-%m-%d %H:%M:%S')}\n")
        file.write(f"Income: ${income:.2f}\n")
        for category, amount in budget.items():
            file.write(f"• {category:16} ${amount:8.2f}\n")
        file.write("_" * 40+ "\n")

if __name__ == "__main__":
    _self_test()
    main_menu()

f.write("✅ Session 4 Complete: Menu, M odular Functions, REPORT_PATH.\N")
