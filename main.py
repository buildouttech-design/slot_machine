MAX_LINES = 3
def deposit():
    print("Welcome to the ATM!")
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
    return amount

def get_number_of_lines():
    while True:
        lines = input(
            "Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines.")
        else:
            print("Please enter a number.")

    return lines
        

def main():
   balance = deposit()
   lines = get_number_of_lines()
   print(f"You have chosen to bet {balance} on {lines} lines.")
    


main()