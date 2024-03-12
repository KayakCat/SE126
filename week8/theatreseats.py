# Simplified variables
columns = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234"
rows = [["#"] * len(columns) for _ in range(15)]
cart = []

# Functions
def seating_chart():
    #print the header for the seating chart
    print("Rows\tSeats")

    #initialize the row number
    row_number = 1

    # Loop through each row in the 'rows' list
    for row in rows:
        # Combine seat symbols in the row, using ".join() and separating with spaces
        seats_string = " ".join(row)
        # Print the current row number and its corresponding seats
        print(f"{row_number}\t{seats_string}")
        
        row_number += 1


def get_input(prompt, validation_func):
    while True:
        try:
            user_input = validation_func(input(prompt))
            return user_input
        except ValueError as e:
            print(e)

def get_row_input():
    return get_input("Please enter the row number (1-15): ", lambda x: int(x) - 1)

def get_column_input():
    return get_input("Please enter the seat letter (A-4): ", lambda x: x.upper())

def is_seat_available(row, column):
    return rows[row][columns.index(column)] == "#"

def add_to_cart():
    row = get_row_input()
    column = get_column_input()

    if (row, column) in cart:
        print("Seat is already in cart")
    elif not is_seat_available(row, column):
        print("Seat is not available")
    else:
        cart.append((row, column))
        rows[row][columns.index(column)] = "*"  # Mark seat as taken

    if input("\nWould you like to add another seat? (y/n): ").lower() == "y":
        add_to_cart()

def view_total_seat_sales():
    for i in range(len(rows)):
        for j in range(len(columns)):
            seat = rows[i][j]
            if seat == "*":
                price = 200 if i < 6 else (175 if i < 11 else 150)
                print(f"Seat {columns[j]} in row {i+1} - ${price}")

# Other functions (unchanged)

# Main program loop
def prompt_menu():
    print("\n\n\t\t\t\tMenu:\n")
    print("1. Display Seats")
    print("2. Add to cart")
    print("3. View Total Seat Sales")
    print("4. View Seat Information")
    print("5. Checkout")
    print("6. Exit")

    while True:
        try:
            answer = int(input("\n\t\t\tPlease select an option: "))
            if answer not in [1, 2, 3, 4, 5, 6]:
                print("Please select a valid option")
            else:
                return answer
        except ValueError:
            print("Please enter a number")

def handle_answer(answer):
    if answer == 1:
        seating_chart()
    elif answer == 2:
        add_to_cart()
    elif answer == 3:
        view_total_seat_sales()
    elif answer == 4:
        view_seat_information()
    elif answer == 5:
        checkout()
    else:
        print("Thank you for using the program")
        exit()

answer = None
while answer != 6:
    answer = prompt_menu()
    handle_answer(answer)