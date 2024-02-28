#Latoya Hall
#week7hw.py

#------------------LIBRARIES-------------------------------------------------
import csv

#--------------------MAIN CODE-----------------------------------------------
#create empty 1d lists to hold data in the text file
student_ids = []
lnames = []
fnames = []
class1 = []
class2 = []
class3 = []

#initialize counters
records = 0 #holds the total number of records in file/each list
search_count = 0 #holds the count of search loops (how many search loops were used to find the item we are looking for)

with open("week7/lab5_students.txt") as csvfile:

    file = csv.reader(csvfile)

    for rec in file:
        records += 1

        student_ids.append(rec[0])
        lnames.append(rec[1])
        fnames.append(rec[2])
        class1.append(rec[3])
        class2.append(rec[4])
        class3.append(rec[5])


# function for getting user input for choice
def class_menu():
    print("\n NEIT Student Class Search")
    print("1. See All Student Report.")
    print("2. Search for a Student by ID  Number")
    print("3. Search for a Student by Last Name")
    print("4. View a Class Roster[Class 1, Class 2, and Class 3]")
    print("5. Exit/Quit Program")

     # Get the user's input (choice) to navigate the menu
    choice = input("Enter your choice (1, 2, 3, 4, or 5): ")

    # Loop to trap the user if they don't follow the directions
    while choice not in ['1', '2', '3', '4', '5']:
        print("*INVALID ENTRY* Enter 1, 2, 3, 4, or 5 only.")
        choice = input("Enter your choice (1, 2, 3, 4, or 5): ")

    return choice


#function to print header
def header():
    print(f"{'Student ID':4}\t{'Last Name':12}\t{'First Name':12}\t{'Class 1':3}\t{'Class 2':3}\t{'Class 3':3}")
    spacer()


#function to print a spacer
def spacer():
    print("-" * 75)


#function to print records
def print_record(index):
    print(f"{student_ids[index]:6}\t\t{lnames[index]:12}\t{fnames[index]:12}\t{class1[index]:3}\t{class2[index]:3}\t{class3[index]:3}")


# function to display all students
def display_all():
    header()

    for i in range (0, len(student_ids)):
        print_record(i)

    spacer()


# function to search for students in a class
def class_search():
    search_value = input("which class do you want to find: ").upper()

    header()
    for i in range(len(class1)):
        if search_value in [class1[i], class2[i], class3[i]]:
            print_record(i)
    spacer()


# function to search through an input using binary search
def binary_search(question, input_array):
    search = input(f"{question}?: ").lower()
    min = 0
    max = records - 1
    guess = int((min + max) / 2)

    while (min < max and search != input_array[guess]):
        if search < input_array[guess]:
            max = guess - 1

        else:
            min = guess + 1

        guess = int((min + max) / 2)

        if search == input_array[guess].lower():
            header()
            print_record(guess)
            spacer()

        else:
            continue


def main():
        
    running = True
    while running:
        answer = int(class_menu())

        if answer == 1:
            display_all()

        elif answer == 2:
            binary_search("what student ID do you want to see", student_ids)

        elif answer == 3:
            binary_search("what last name do you want to see", lnames)

        elif answer == 4:
            class_search()

        elif answer == 5:
            running = False


if __name__ == "__main__":
    main()
