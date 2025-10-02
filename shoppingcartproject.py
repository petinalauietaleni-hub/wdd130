# Creative Enhancement: I added quantity tracking for each item and formatted the cart display using aligned columns for item number, name, quantity, and price.

cart_items = []
cart_prices = []
cart_quantities = []

print("Welcome to the Shopping Cart Program!")

while True:
    print("\nPlease select one of the following:")
    print("1. Add item")
    print("2. View cart")
    print("3. Remove item")
    print("4. Compute total")
    print("5. Quit")

    choice = input("Please enter an action: ")

    if choice == "1":
        item = input("What item would you like to add? ")
        price = float(input(f"What is the price of '{item}'? "))
        quantity = int(input(f"How many '{item}' would you like to add? "))
        cart_items.append(item)
        cart_prices.append(price)
        cart_quantities.append(quantity)
        print(f"{quantity} '{item}' added to the cart.")

    elif choice == "2":
        print("\nThe contents of the shopping cart are:")
        print(f"{'No.':<5}{'Item':<15}{'Qty':<5}{'Price':>10}")
        for i in range(len(cart_items)):
            print(f"{i+1:<5}{cart_items[i]:<15}{cart_quantities[i]:<5}${cart_prices[i]:>9.2f}")

    elif choice == "3":
        print("\nThe contents of the shopping cart are:")
        print(f"{'No.':<5}{'Item':<15}{'Qty':<5}{'Price':>10}")
        for i in range(len(cart_items)):
            print(f"{i+1:<5}{cart_items[i]:<15}{cart_quantities[i]:<5}${cart_prices[i]:>9.2f}")
        index = int(input("Which item would you like to remove? ")) - 1
        if 0 <= index < len(cart_items):
            removed_item = cart_items.pop(index)
            cart_prices.pop(index)
            cart_quantities.pop(index)
            print(f"'{removed_item}' has been removed.")
        else:
            print("Sorry, that is not a valid item number.")

    elif choice == "4":
        total = 0
        for i in range(len(cart_prices)):
            total += cart_prices[i] * cart_quantities[i]
        print(f"\nThe total price of the items in the shopping cart is ${total:.2f}")

    elif choice == "5":
        print("Thank you. Goodbye.")
        break

    else:
        print("Invalid option. Please try again.")