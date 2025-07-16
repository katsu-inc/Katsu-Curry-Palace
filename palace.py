def katsu_curry_palace():
    print("Irasshaimase! This is Katsu Curry Palace. Please take a seat!")

    while True:
        response = input("Would you like to take a seat? (yes/no): ").strip().lower()
        if response == "no":
            print("No worries! Hope to see you again soon.")
            return
        elif response == "yes":
            break
        else:
            print("Sorry, I didn't understand that.")

    while True:
        size = input("Great! What size katsu curry would you like? (small/medium/large): ").strip().lower()
        if size in ["small", "medium", "large"]:
            print(f"You've selected a {size} katsu curry. Great choice!")
            break
        else:
            print("Sorry, please choose from small, medium, or large.") 

    toppings_list = ["extra chicken", "cheese", "egg", "spring onions", "spicy mayo"]
    print("\nHere are our available toppings:")
    for i, topping in enumerate(toppings_list, 1):
        print(f"{i}. {topping.title()}")

    print("You can choose multiple toppings separated by commas (e.g., 1,3,5) or press Enter to skip.")

    while True:
        topping_input = input("Which toppings would you like? ").strip()
        if topping_input == "":
            selected_toppings = []
            break
        else:
            try:
                indexes = [int(i) for i in topping_input.split(",") if i.strip().isdigit()]
                if all(1 <= idx <= len(toppings_list) for idx in indexes):
                    selected_toppings = [toppings_list[i - 1] for i in indexes]
                    break
                else:
                    print("Some numbers were out of range. Please try again.")
            except ValueError:
                print("Invalid input. Please enter numbers separated by commas.")

print("Thank you for your order. Enjoy your katsu curry from Katsu Curry Palace! Arigatou gozaimashita!")