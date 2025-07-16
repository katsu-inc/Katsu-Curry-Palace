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
    #ghp_ZmxhZ3tjb21taXRtZW50X2lzc3Vlc30gICAg
    for i, topping in enumerate(toppings_list, 1):
        print(f"{i}. {topping.title()}")

print("Thank you for your order. Enjoy your katsu curry from Katsu Curry Palace! Arigatou gozaimashita!")