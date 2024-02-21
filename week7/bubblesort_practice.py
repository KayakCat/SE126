#w7d2 - bubble sort and binary search

import csv

#create empty 1D list
type_ = []
name = []
meaning = []
origin = []

with open ("week7/party.csv", encoding="utf-8") as csvfile:
    file = csv.reader(csvfile)

    for rec in file:
        type_.append(rec[0])
        name.append(rec[1])
        meaning.append(rec[2])
        origin.append(rec[3])

#original file print
        
print(f"{'TYPE':8} {'NAME':12} {'MEANING':30} {'ORIGIN'}")
for i in range(0, len(type_)):
    print(f"{type_[i]:8} {name[i]:12} {meaning[i]:30} {origin[i]}")

#sort the file data by first name, ascending (increasing order)
#--------------------------------------------------------------
#Bubble sort ---------------------------------------------------
        
for i in range(0, len(name) - 1):#outer loop


    for index in range(0, len(name) - 1):#inner loop
      

        #below if statement determines the sort

        #list used is the list being sorted

        # > is for increasing order, < for decreasing

        if(name[index] > name[index + 1]):


            #if above is true, swap places!

            temp = name[index]
            name[index] = name[index + 1]
            name[index + 1] = temp

 
            #swap all other values
            #type--------------
            temp = type_[index]
            type_[index] = type_[index + 1]
            type_[index + 1] = temp

            #swap all other values
            #meaning--------------
            temp = meaning[index]
            meaning[index] = meaning[index + 1]
            meaning[index + 1] = temp

            #swap all other values
            #origin--------------
            temp = origin[index]
            origin[index] = origin[index + 1]
            origin[index + 1] = temp
print("-------------------------------------------------------------")
print(f"{'TYPE':8} {'NAME':12} {'MEANING':30} {'ORIGIN'}")
for i in range(0, len(type_)):
    print(f"{type_[i]:8} {name[i]:12} {meaning[i]:30} {origin[i]}")








#create loop for user to repeatedly search through
#perform binary search
#Binary Search---------------------------------------------------
    
#Binary Search Algorithm:

search = input("Get search from user!")

min = 0

max = len(name) - 1       #can also use len(listName) for 'records' value


mid = int((min + max) / 2)

#this is for INCREASING order ---this is the searching loop

while (min < max and search.lower != name[mid].lower):

   if search < name[mid]:

       max = mid - 1

   else:

       min = mid + 1

   mid = input((min + max) / 2)

if search.lower == name[mid].lower:

    #found them! use 'mid' for index of found search item
    print(f"\n\tWe found {search}! Here is their info:")
    print("-------------------------------------------------------------")
    print(f"{'TYPE':8} {'NAME':12} {'MEANING':30} {'ORIGIN'}")
    print(f"{type_[mid]:8} {name[mid]:12} {meaning[mid]:30} {origin[mid]}")
else:

    #boooo not found
    print(f"\n\tWe DID NOT find {search}! Try again!")

answer = input("Would you like to search again? [y/n]: ")