#Latoya Hall
#week7hw.py

#------------------VARIABLE DICTIONARY---------------------------------------

#------------------FUNCTIONS-------------------------------------------------
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


#------------------LIBRARIES-------------------------------------------------
import csv
#--------------------MAIN CODE------------------------------------------------

#create empty 1d lists to hold data in the text file
student_id = []
lname = []
fname = []
class1 = []
class2 = []
class3 = []

with open("week7/lab5_students.txt") as csvfile:

    file = csv.reader(csvfile)

    for rec in file:
        student_id.append(rec[0])
        lname.append(rec[1])
        fname.append(rec[2])
        class1.append(rec[3])
        class2.append(rec[4])
        class3.append(rec[5])
print(f"{'Student ID':6}\t{'Last Name':12}\t{'First Name':12}\t{'Class 1':3}\t{'Class 2':3}\t{'Class 4':3}")
print("-------------------------------------------------------------------------------------------------")
for i in range (0, len(student_id)):
    print(f"{student_id[i]:6}\t{lname[i]:12}\t{fname[i]:12}\t{class1[i]:3}\t{class2[i]:3}\t{class3[i]:3}")
("----------------------------------------------------------------------------------------")
choice = '0'

while choice != '4':

    choice = class_menu() #calling the menu into the loop



