#----------------variable dictionary-------------------------------------
#running_total          cumulative sum that keeps track of classes as they are added
#current_total          total of classes that have been added so far
#def hello              function to welcome clients
#def goodbye            function that says goodbye to clients
#def swap               function that makes the bubble sort function way heckin' easier
#def reserve_spot       function that keeps track of spots available in classes
#def book               function that holds a loop to calculate cost of user choices
#def menu               function that holds the menu for user to book classes
#choice                 variable to get user input 
#while choice           loop to trap user if they make an invalid selection
#num_rec                variable to count records
#client_id              client id number
#first                  client first name
#last                   client last name
#email                  client email
#phone                  client phone number
#
               



#----------------functions------------------------------------------------

#vars used globally 
running_total = 0
current_total = 0

def hello():

    print("Welcome to the Zen Den")

def goodbye():

    print("Thank you for choosing the Zen Den! Namaste.")

#a function that swaps values for bubble sorting
def swap(items, posi):
    #posi --> current position (index) of where swap needs to occur
    
    temp = items[posi]
    items[posi] = items[posi + 1]
    items[posi + 1] = temp



def reserve_spot(obj_name, str_name):

    if obj_name[str_name] == 0:
        print(f"Sorry, the {obj_name['name']} does not have any available spots left :[")
    else:
        obj_name[str_name] -= 1
        print(f"You have been booked for {obj_name['name']} class! Enjoy!")

def book(obj_name):
    if obj_name == standard_class:
        running_total += 20
        current_total += 20

    if obj_name == meditation_class:
        running_total += 35
        current_total += 35

    if obj_name == walking_meditation_class:
        running_total += 25
        current_total += 25

    if obj_name == class_package:
        running_total += 180
        current_total += 180

    else:
        print(f"Sorry you have made an invalid selection")
     

def menu():
    print("\n--Zen Den Menu--")
    print("1. Book Drop-In Yoga Class")
    print("2. Book Healing Meditation Journey")
    print("3. Book Walking Meditation Chakra Balancing")
    print("4. Purchase 10 Class Yoga Package")
    print("5. Exit")

    # Get the user's input (choice) to navigate the menu
    choice = input("Enter your choice (1, 2, 3, 4, or 5): ")

    # Loop to trap the user if they don't follow the directions
    while choice not in ['1', '2', '3', '4', '5']:
        print("*INVALID ENTRY* Enter 1, 2, 3, 4, or 5 only.")
        choice = input("Enter your choice (1, 2, 3, 4, or 5): ")

    return choice

#------------------main code-----------------------------------------------
num_rec = 0

import csv
client_id = []
first = []
last = []
email = []
phone = []



with open("week9/clientrecords.txt")as csvfile:

    file = csv.reader(csvfile)

    #when reading files, each record is treated as a list
    #each field of data (rec[#]) represents a new value
    for rec in file:

        #this for loop will run for as many records (rows) of data in the file

        #store data into lists --> .append()
        client_id.append(rec[0])
        first.append(rec[1])
        last.append(rec[2])
        email.append(rec[3])
        phone.append(rec[4])

        num_rec += 1
print("-----------------------------------------------------------------------------------------------------")
print(f"{'ID':3}\t{'First':15}\t{'Last':15}\t\t{'Email':35}\t{'Phone':10}")
print("----------------------------------------------------------------------------------------------------")
for i in range(0, num_rec):

    print(f"{client_id[i]:3}\t{first[i]:15}\t{last[i]:15}\t\t{email[i]:25}\t\t{phone[i]:10}\t")
#--------------------bubble sort------------------------------------------------------------
search = input("\n\twhich first name are you looking for?")
for i in range(0, len(first) - 1):
    for k in range(0, len(first) - 1):
        if first[k] > first[k + 1]:

            #swap values
            first_swap = first[k]
            first[k] = first[k + 1]
            first[k + 1] = first_swap

             #swap values
            swap(client_id, k)
            swap(first, k)
            swap(last, k)
            swap(email, k)
            swap(phone, k)
            
#----------------binary sort----------------------------------------------------------------

        min = 0
        max = len(first) - 1
        mid = int((min + max) / 2)

        while min < max and search != first[mid]:
            if int(search) > mid:
                min = mid + 1

            else:
                max = mid - 1

                mid = int((min + max) / 2)
            
         #print results
            if search == first[mid]:
                print(f"we found your search for {search}")

                print(f"{client_id[mid]:10}\t{first[mid].upper():15}\t{last[mid]:15}\t{email[mid]:35}\t{phone[mid]:7}")

            else:
                print(f"womp womp we could not find {search}")




#variable to establish that each class has five available spots
available_spots = 5

#class dictionary that pairs the class/offering with it's pricing/time/availabe spots
standard_class = {
"name": "Drop-In Yoga Class",
"time": "7:30A",
"available_spots": 5,
"cost": 20
}


print(standard_class["name"]) 
#print("Available Spots:",standard_class["available_spots"] -= 1 )#would remove 1 from 5

meditation_class = {
"name": "Healing Meditation Journey",
"time": "6:30P",
"available_spots": 5,
"cost": 35
}

print(meditation_class["name"]) 
#print(f"Available Spots:",meditation_class["available_spots"] -= 1 )#would remove 1 from 5


walking_meditation_class = {
    "name": "Walking Meditation Chakra Balancing",
    "time": "2:00P",
    "available_spots": 5,
    "cost": 25
}

print(walking_meditation_class["name"])
print(f"Available Spots:",walking_meditation_class["available_spots"])
walking_meditation_class["available_spots"] -= 1 #would remove 1 from 5

print(f"Available Spots:",walking_meditation_class["available_spots"])

class_package = {
    "name": "Yoga - 10 Class Package",
    "time": "Flexible",
    "number of classes": 10,
    "available_spots": None,
    "cost": 180
}
print(f"Thank you for purchasing a 10 Class Package: {class_package['time']}")


reserve_spot(standard_class, "available_spots")

print(f"Available Spots:",standard_class["available_spots"])

print(f"Your total balance is: {running_total:.2f}")



