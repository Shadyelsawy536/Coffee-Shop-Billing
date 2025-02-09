import datetime

MENU = {
    1: {"name": "Tea", "price": 10},
    2: {"name": "Coffee", "price": 20},
    3: {"name": "Water", "price": 5}
}

def display_menu():
    print("\n Coffee Shop Menu:")
    for num, item in MENU.items():
        print(f"    {num}. {item['name']} - {item['price']} LE")

def get_valid_input(prompt, valid_options):
    """Handles user input validation"""
    while True:
        try:
            value = int(input(prompt))
            if value in valid_options:
                return value
            print(" Invalid choice, please try again.")
        except ValueError:
            print(" Invalid input, please enter a number.")

def calculate_total(price, quantity, tax_rate=0.1):
    order_cost = price * quantity
    tax = order_cost * tax_rate
    return order_cost, tax, order_cost + tax
def print_receipt(drink_name, quantity, price, order_cost, tax, total):
    """Prints the receipt"""
    timestamp = datetime.datetime.now().strftime('%c')
    receipt = (
        f"\n  Receipt  \n"
        f" Date: {timestamp}\n"
        f" Drink: {drink_name}\n"
        f" Quantity: {quantity}\n"
        f" Price per unit: {price} LE\n"
        f" Order Total: {order_cost} LE\n"
        f" Tax (10%): {tax:.2f} LE\n"
        f" Final Total: {total:.2f} LE\n"
    )
    print(receipt)

def main():
    display_menu()
    drink_choice = get_valid_input("\nChoose Drink Number (1, 2, 3) from the menu: ", MENU.keys())
    quantity = get_valid_input("Enter Drink Quantity: ", range(1, 101))  # Limit max quantity to 100 for safety

    drink_name = MENU[drink_choice]["name"]
    price = MENU[drink_choice]["price"]
    order_cost, tax, total = calculate_total(price, quantity)

    print_receipt(drink_name, quantity, price, order_cost, tax, total)

if __name__ == "__main__":
    main()
