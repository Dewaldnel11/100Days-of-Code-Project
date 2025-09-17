from typing import Dict, Optional
MENU = {
    "espresso": {
        "ingredients": {
            "coffee": 24,
        },
        "cost": 3.0,
    },
}
COIN_VALUES = {
    "nickels": 5,
    "pennies": 1,
}
INITIAL_RESOURCES = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
profit_cents = 0
resources: Dict[str, int] = INITIAL_RESOURCES.copy()
def display_menu() -> None:
    print("Available drinks:")
    for drink_name, details in MENU.items():
        cost = details["cost"]
        ingredients_description = ", ".join(
            f"{ingredient} {amount}{'ml' if ingredient in {'water', 'milk'} else 'g'}"
            for ingredient, amount in details["ingredients"].items()
        )
        print(f"- {drink_name.title()} (${cost:.2f}) -> {ingredients_description}")
def print_report() -> None:
    print(f"Water: {resources.get('water', 0)}ml")
    print(f"Milk: {resources.get('milk', 0)}ml")
    print(f"Coffee: {resources.get('coffee', 0)}g")
    print(f"Money: ${profit_cents / 100:.2f}")
def reset_resources() -> None:
    resources.clear()
    resources.update(INITIAL_RESOURCES)
    print("Resources have been reset to their default levels.")
def is_resource_sufficient(order_ingredients: Dict[str, int]) -> bool:
    """Return True when order can be made, False when ingredients are insufficient."""
    shortages = []
    for item, required_amount in order_ingredients.items():
        available_amount = resources.get(item, 0)
        if required_amount > available_amount:
            shortages.append((item, required_amount - available_amount))
    if shortages:
        for item, deficit in shortages:
            unit = "ml" if item in {"water", "milk"} else "g"
            print(f"Sorry, there is not enough {item}. Need {deficit}{unit} more.")
        return False
    return True
def _prompt_for_int(
    prompt: str,
    *,
    allow_blank: bool = False,
    minimum: int = 0,
) -> Optional[int]:
    while True:
        response = input(prompt).strip()
        if allow_blank and response == "":
            return None
        try:
            value = int(response)
        except ValueError:
            print("Sorry, that's not a valid number. Please try again.")
            continue
        if value < minimum:
            print(f"Please enter a number greater than or equal to {minimum}.")
            continue
        return value
def _prompt_for_coin_count(prompt: str) -> int:
    value = _prompt_for_int(prompt, minimum=0)
    return 0 if value is None else value
def process_coins() -> int:
    print("Please insert coins.")
    total_cents = 0
    for coin, value in COIN_VALUES.items():
        count = _prompt_for_coin_count(f"How many {coin}?: ")
        total_cents += count * value
    return total_cents
def process_coins() -> int:

    print("Please insert coins.")
    total_cents = 0
    for coin, value in COIN_VALUES.items():
    return total_cents
def is_transaction_successful(money_received_cents: int, drink_cost_dollars: float) -> bool:
    """Return True when the payment is accepted, False if money is insufficient."""
    drink_cost_cents = int(round(drink_cost_dollars * 100))
    if money_received_cents >= drink_cost_cents:
        change_cents = money_received_cents - drink_cost_cents
        global profit_cents
        profit_cents += drink_cost_cents
        return True
    print("Sorry, that's not enough money. Money refunded.")
    return False
def make_coffee(drink_name: str, order_ingredients: Dict[str, int]) -> None:
    """Deduct the required ingredients from the resources."""
    for item, amount in order_ingredients.items():
        resources[item] = resources.get(item, 0) - amount
    print(f"Here is your {drink_name} ☕️. Enjoy!")
def refill_resources() -> None:
    print("Refilling resources. Press Enter to skip a resource.")
    for item in sorted(resources):
        addition = _prompt_for_int(
            f"Additional {item} to add (current {resources[item]}): ",
            allow_blank=True,
            minimum=0,
        )
        if addition is not None:
            resources[item] += addition
    print("Resources updated.")
def print_help() -> None:
    print("Commands: espresso, latte, cappuccino, report, menu, refill, reset, help, off")
COMMAND_ALIASES = {
    "quit": "off",
    "exit": "off",
    "status": "report",
    "restock": "refill",
}
def normalize_choice(choice: str) -> str:
    return COMMAND_ALIASES.get(choice, choice)
def run_machine() -> None:
    while True:
        try:
            choice_raw = input("What would you like? (espresso/latte/cappuccino): ")
        except (EOFError, KeyboardInterrupt):
            print("\nPowering down coffee machine.")
            break
        choice = choice_raw.strip().lower()
        if not choice:
            print("Please enter a drink selection.")
            continue
        choice = normalize_choice(choice)
        if choice == "off":
            print("Powering down coffee machine.")
            break
        if choice == "help":
            print_help()
            continue
        if choice == "menu":
            display_menu()
            continue
        if choice == "report":
            print_report()
            continue
        if choice == "refill":
            refill_resources()
            continue
        if choice == "reset":
            reset_resources()
            continue
        if choice in MENU:
            drink = MENU[choice]
            if is_resource_sufficient(drink["ingredients"]):
                payment_cents = process_coins()
                if is_transaction_successful(payment_cents, drink["cost"]):
                    make_coffee(choice, drink["ingredients"])
            continue
        print("Sorry, we don't serve that selection. Type 'help' to see available options.")
if __name__ == "__main__":
    run_machine()