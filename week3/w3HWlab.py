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

print(f"{'ID NUMBER':4}      {'AGE':6}        {'REGISTERED TO VOTE':6} {'DID THEY VOTE':6}")
print("------------------------------------------------------------------------------")

with open("lab3HW.csv") as csvfile:

    file = csv.reader(csvfile)

    for rec in file:

        # keep track of the rec count in the file
        total_records += 1

        # convert age to integer for comparison
        age = int(rec[1])

        #filter for display------------------------------------------------

        if rec[1] < "18":
            ineligible += 1
        elif rec[2] =="N":
            unreg += 1
        elif rec[2] == "Y" and rec[3] == "N":   
            eligible_not_voted += 1
        else:
            has_voted == "Y"
            votes  += 1

        #append respective values to the appropriate field list
        id_number_list.append(rec[0])
        age_list.append(age)
        registered_list.append(rec[2])
        has_voted_list.append(has_voted)

for index in range(0, total_records):
    #for index in range(0, len(comp_type_list)): --> len(comp_type_list) returns the INTEGER count of values
    print(f"{id_number_list[index]:4} {age_list[index]:6} {registered_list[index]:6} {has_voted_list[index]:6}")


    
print(f"Total records entered: {total_records}")
print(f"Total of people ineligible to register to vote: {ineligible}")
print(f"Total of people eligible to vote but are not registered: {unreg}")
print(f"Total of people eligible and registered, but did not vote: {eligible_not_voted}")
print(f"Total of people eligible, registered, and placed a vote: {votes}")

print("\n\n\nThank you for using the program. Goodbye!")
