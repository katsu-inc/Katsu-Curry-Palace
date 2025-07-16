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

    meal_sides = ["edamame", "miso soup", "soft drink", "green tea"]
    print("\nWould you like to make it a meal? It comes with one side.")
    while True:
        meal_choice = input("Would you like a meal? (yes/no): ").strip().lower()
        if meal_choice == "no":
            selected_side = None
            break
        elif meal_choice == "yes":
            print("\nHere are the available sides:")
            for i, side in enumerate(meal_sides, 1):
                print(f"{i}. {side.title()}")
            while True:
                side_input = input("Please choose a side by number (e.g., 2): ").strip()
                if side_input.isdigit() and 1 <= int(side_input) <= len(meal_sides):
                    selected_side = meal_sides[int(side_input) - 1]
                    break
                else:
                    print("Invalid selection. Please enter a number from the list.")

            while True:
                upsize_input = input("Would you like to upsize your meal? (yes/no): ").strip().lower()
                if upsize_input in ["yes", "no"]:
                    upsized = (upsize_input == "yes")
                    break
                else:
                    print("Please answer 'yes' or 'no'.")
            break
        else:
            print("Please answer 'yes' or 'no'.")

print("Thank you for your order. Enjoy your katsu curry from Katsu Curry Palace! Arigatou gozaimashita!")