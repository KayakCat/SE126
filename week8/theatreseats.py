# Define constants
SEAT_AVAILABLE = '#'
SEAT_TAKEN = '*'

# Function to display the seating chart
def display_seating_chart(seats):
    # Print header
    print("  ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    # Print rows
    for i, row in enumerate(seats, start=1):
        print(f"{i:2} {' '.join(row)}")

# Function to allow the user to select a seat
def select_seat(seats):
    # Display seating chart
    display_seating_chart(seats)

    # Loop until user finishes selecting seats
    while True:
        row = get_valid_row_input(len(seats))
        seat = get_valid_seat_letter_input()

        if seats[row][ord(seat) - ord('A')] == SEAT_AVAILABLE:
            seats[row][ord(seat) - ord('A')] = SEAT_TAKEN
            print("Seat selected successfully.")
        else:
            print("Sorry, that seat is already taken. Please choose another seat.")

        # Check if user wants to select another seat
        choice = input("Do you want to select another seat? (y/n): ").lower()
        if choice != 'y':
            break

    return seats

# Function to get a valid row input
def get_valid_row_input(num_rows):
    while True:
        try:
            row = int(input(f"Enter the row number (1-{num_rows}): ")) - 1
            if 0 <= row < num_rows:
                return row
            else:
                print(f"Invalid row number. Please enter a number between 1 and {num_rows}.")
        except ValueError:
            print("Invalid input. Please enter a valid row number.")

# Function to get a valid seat letter input
def get_valid_seat_letter_input():
    while True:
        seat = input("Enter the seat letter (A-Z): ").upper()
        if 'A' <= seat <= 'Z':
            return seat
        else:
            print("Invalid seat letter. Please enter a letter from A to Z.")

# Main program
def main():
    # Initialize theater seating chart
    num_rows = 15
    num_seats_per_row = 30
    theater_seats = [[SEAT_AVAILABLE] * num_seats_per_row for _ in range(num_rows)]

    while True:
        print("\nMenu:")
        print("1. Select Seat(s)")
        print("2. View Seating Chart")
        print("3. Quit")

        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            theater_seats = select_seat(theater_seats)
        elif choice == '2':
            display_seating_chart(theater_seats)
        elif choice == '3':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 3.")

if __name__ == "__main__":
    main()
