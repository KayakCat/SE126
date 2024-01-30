#Latoya Hall
#Lab 5A
#Hall_Latoya_Lab5a.py


#         Variable Dictionary

#         ineligible                 a person who is not legal voting age
#         registered                 a person who is registered to vote
#         unreg                      a person who is old enough to vote but is not         registered
#         votes                      indicates a vote that was placed
#         total_records              total records processed 
#         eligible_not_voted         a person who is registered to vote but did not vote
#         voter_record_input         used to identify when a user inputs yes or no to go back into the loop
#===========================================================================================================================
import csv

#total counter for all records
total_records = 0
ineligible = 0
unreg = 0
registered = 0
votes = 0
eligible_not_voted = 0
has_voted = 0
id_number = 0
age = 0
voter_record_input = "Y"

#create some lists - one for EACH potential field in file
id_number_list =[]
age_list =[]
registered_list =[]
has_voted_list =[]

print(f"{'ID NUMBER':10} {'AGE':5} {'REGISTERED':5} {'VOTED (Y/N)':5}")
print("------------------------------------------------------------------------------")

with open("week3/lab3HW.csv") as csvfile:

    file = csv.reader(csvfile)

    for rec in file:

        # keep track of the rec count in the file
        total_records += 1

        # convert age to integer for comparison
        age = int(rec[1])

        #filter for display------------------------------------------------

        if rec[1] < "18": #filters eligibility by age, if under 18 ineligible
            ineligible += 1
            has_voted = "N"
        elif rec[2] =="N": #filters if they have registered to vote or not
            unreg += 1
            has_voted = "N"
        elif rec[2] == "Y": #filters that yes they registered to vote but they did not vote
            if rec[3] == "N":
             eligible_not_voted += 1
             has_voted = "N"  #Displays "N" if registered but did not vote
            else:
             votes += 1 #else statement is for those who are eligible, registered, and voted
             has_voted = "Y"  #Displays "Y" if registered and voted
            
        #append respective values to the appropriate field list
        id_number_list.append(rec[0])
        age_list.append(age)
        registered_list.append(rec[2])
        has_voted_list.append(has_voted)

for index in range(0, total_records): #print the records in a neat format
    
    #printing each field in a neat format by id number, age, registered (Y/N), and has voted (Y/N).
    print(f"{id_number_list[index]:<10} {age_list[index]:<10} {registered_list[index]:<10} {has_voted_list[index]:<10}")



    
print(f"Total records entered: {total_records}")
print(f"Total of people ineligible to register to vote: {ineligible}")
print(f"Total of people eligible to vote but are not registered: {unreg}")
print(f"Total of people eligible and registered, but did not vote: {eligible_not_voted}")
print(f"Total of people eligible, registered, and placed a vote: {votes}")

print("\n\n\nThank you for using the program. Goodbye!")
