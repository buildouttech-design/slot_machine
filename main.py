def deposit():
    while True:
        try:
            amount = float(input("Enter amount to deposit: "))
            if amount <= 0:
                print("Please enter a positive number.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a number.")
    print(f"You have deposited: {amount}")

deposit()