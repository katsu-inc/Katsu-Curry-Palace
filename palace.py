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

print("Thank you for your order. Enjoy your katsu curry from Katsu Curry Palace! Arigatou gozaimashita!")