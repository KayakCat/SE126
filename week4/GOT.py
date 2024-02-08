#Latoya Hall
#2/7/2024
#GOT.py
#----------------VARIABLE DICTIONARY------------------------------------
#fname              first name of people in csv file
#lname              last name of people in csv file    
#age                age of people in csv file
#nname              nickname of people in csv file
#alleg              house the people in the file have allegiance to
#house              variable used in for loop to tie houses to alleg from the file
#motto              variable used to store whichever selection is made in the for loop to identify the motto tied to the allegiance of each house
#stark_tally        used to assign value to tally stark house in for loop
#baratheon_tally    used to assign value to tally baratheon house in for loop
#tully_tally        used to assign value to tally tully house in for loop
#nightswatch_tally  used to assign value to tally nights watch house in for loop
#lannister_tally    used to assign value to tally lannister house in for loop
#targaryen_tally    used to assign value to tally targaryen house in for loop
#total_people       total number of people in the file
#total_age          age of everyone in the file added up together
#average_age        total_age / total_people equals the average age of everyone in the file
#--------------------MAIN PROGRAM------------------------------------------
import csv

#create 1D lists [will be parallel to each other]
#base lists on fields in file

fname = []
lname = []
age = []
nname = []
alleg = []

 #connect to file and read data into 1D lists 
with open ("week4/files/lab4A_GOT_NEW.txt") as csvfile:

    file = csv.reader(csvfile)

    for rec in file:

        #store data from file fields to their respective lists
        fname.append(rec[0])
        lname.append(rec[1])
        age.append(int(rec[2]))
        nname.append(rec[3])
        alleg.append(rec[4])

#disconnected from file----------------------------------------
print(f"{'FIRST':12} \t {'LAST':12} \t {'AGE':3} \t {'NICKNAME':18} \t {'HOUSE':15}")
print("--------------------------------------------------------------------------------")

#process list in for loop
for i in range(0, len(fname)):

    print(f"{fname[i]:12} \t {lname[i]:12} \t {age[i]:3} \t {nname[i]:18} \t {alleg[i]:15}")

#print headers for each column of data
print(f"{'FIRST':12} \t {'LAST':12} \t {'AGE':3} \t {'NICKNAME':18} \t {'HOUSE':15} \t{'MOTTO':25}")
print("---------------------------------------------------------------------------------------------------")

#for loop to match houses with their mottos
for i in range(0, len(fname)):
    house = alleg[i] #creating variable for house using alleg[i]
    motto = "" #variable for motto using "" to store whichever selection is made in the for loop
    

    if house == "House Stark":
        motto = "Winter is Coming"

    elif house == "House Baratheon":
        motto = "Ours is the fury"

    elif house == "House Tully":
        motto = "Family. Duty. Honor."

    elif house == "Nights Watch":
        motto = "And now my watch begins."

    elif house == "House Lannister":
        motto = "Hear Me Roar"

    else:
        house ="House Targaryen"
        motto = "Fire and Blood"

    

    #print list which now includes the motto for each house along with previous data
    print(f"{fname[i]:12} \t {lname[i]:12} \t {age[i]:3} \t {nname[i]:18} \t {alleg[i]:15} \t {motto:25}")
#create variables to tally each house
stark_tally = 0
baratheon_tally = 0
tully_tally = 0
nightswatch_tally = 0
lannister_tally = 0
targaryen_tally = 0

#for loop using house in alleg to pinpoint exactly which field in the list needs to be looked at to get the proper tally
for house in alleg:
    if house == 'House Stark':
        stark_tally += 1
    elif house == 'House Baratheon':
        baratheon_tally += 1
    elif house == 'House Tully':
        tully_tally += 1
    elif house == 'Nights Watch':
        nightswatch_tally += 1
    elif house == 'House Lannister':
        lannister_tally += 1
    elif house == 'House Targaryen':
        targaryen_tally += 1

print("------------------------------------------------")



total_people = len(fname) #len used so that the entire list can be checked for fname to determine number of peope
total_age = sum(age) #get the total of all ages of people in the file
average_age = total_age / total_people # determine average age by dividing total_age by total_people

# Print the total number of people
print(f"Total number of people of the noble houses: {total_people}")

# Print the average age rounded to a whole number
print(f"Average age: {average_age:.0f}")
print("--------------------------------------------")
# Print allegiance tallies
print("~Allegiance Tallies~")
print(f"House Stark: {stark_tally}")
print(f"House Baratheon: {baratheon_tally}")
print(f"House Tully: {tully_tally}")
print(f"Night's Watch: {nightswatch_tally}")
print(f"House Lannister: {lannister_tally}")
print(f"House Targaryen: {targaryen_tally}")




    

