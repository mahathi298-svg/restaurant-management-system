
# Restaurant Management System

menu = {
    1: {"name": "Burger", "price": 120},
    2: {"name": "Pizza", "price": 250},
    3: {"name": "Sandwich", "price": 100},
    4: {"name": "French Fries", "price": 80},
    5: {"name": "Cold Drink", "price": 40}
}

order = []

def display_menu():
    print("\n========== RESTAURANT MENU ==========")
    for key, item in menu.items():
        print(f"{key}. {item['name']} - Rs.{item['price']}")
    print("=====================================")

def add_item():
    name = input("Enter food item name: ")
    price = float(input("Enter food item price: "))

    item_id = max(menu.keys(), default=0) + 1

    menu[item_id] = {
        "name": name,
        "price": price
    }

    print("Food item added successfully!")

def take_order():
    display_menu()

    while True:
        try:
            choice = int(input("\nEnter item number (0 to finish): "))

            if choice == 0:
                break

            if choice not in menu:
                print("Invalid item number!")
                continue

            quantity = int(input("Enter quantity: "))

            if quantity <= 0:
                print("Quantity must be positive!")
                continue

            item = menu[choice]

            order.append({
                "name": item["name"],
                "price": item["price"],
                "quantity": quantity
            })

            print("Item added to order!")

        except ValueError:
            print("Please enter a valid number.")

def generate_bill():
    if not order:
        print("No orders found!")
        return

    print("\n========== CUSTOMER BILL ==========")

    total = 0

    for item in order:
        amount = item["price"] * item["quantity"]
        total += amount

        print(
            f"{item['name']} x {item['quantity']} "
            f"= Rs.{amount:.2f}"
        )

    gst = total * 0.05
    grand_total = total + gst

    print("-----------------------------------")
    print(f"Subtotal      : Rs.{total:.2f}")
    print(f"GST (5%)      : Rs.{gst:.2f}")
    print("-----------------------------------")
    print(f"Grand Total   : Rs.{grand_total:.2f}")
    print("===================================")

def main():
    while True:
        print("\n====== RESTAURANT MANAGEMENT SYSTEM ======")
        print("1. Display Menu")
        print("2. Add Food Item")
        print("3. Take Customer Order")
        print("4. Generate Bill")
        print("5. Exit")

        try:
            choice = int(input("Enter your choice: "))

            if choice == 1:
                display_menu()

            elif choice == 2:
                add_item()

            elif choice == 3:
                take_order()

            elif choice == 4:
                generate_bill()

            elif choice == 5:
                print("Thank you for visiting!")
                break

            else:
                print("Invalid choice! Try again.")

        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    main()
