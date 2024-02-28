#W7D1 - Comparing Searching Methods Demo
#this demo covers : sequential search (review), Binary search (intro), and bubble sort (intro)

#Libraries---------------------------------------------------------------------------
import csv
#Functions---------------------------------------------------------------------------




#MainProgram--------------------------------------------------------------------------
#create empty 1d lists to hold data in the text file

id_stud = []
lname = []
fname = []
class1 = []
class2 = []
class3 = []

with open ("week7/w7_demoFile.txt") as csvfile:

    file = csv.reader(csvfile)

    for rec in file:

        id_stud.append(rec[0])
        lname.append(rec[1])
        fname.append(rec[2])
        class1.append(rec[3])
        class2.append(rec[4])
        class3.append(rec[5])

#check file connectivity
        
for i in range (0, len(id_stud)):
    print(f"{id_stud[i]}\t{lname[i]}\t{fname[i]}")

#sequential search --- searching in sequencing (from beginning through to the end)
    
search_name = input("Enter the name you are looking for: ")
found = [] #allows for multiples in search
#found = -1
seq_count = 0

#for loop allows review of each value in list (sequence)
for i in range (0, len(lname)):
    seq_count += 1
    #ask if search value matches current value in the list(search)
    if search_name.lower == lname[i].lower():
        #store found value's LOCATION (index)

        found.append(i)

print(f"\n\tsearching complete. search loop ran {seq_count} iterations")
if found:
    print(f"\n\t We found {search_name} at index position(s): {found}")
    print(f"\tHere is their info:")

    for i in range(0, len(found)):
        print(f"\t\t{fname[found[i]]} \t{lname[found[i]]} \t{fname[found[i]]} \t{id_stud[found[i]]} \t{class1[found[i]]} \t{class2[found[i]]} \t{class3[found[i]]}")


else:
     print(f"\n\tWe could not find {search_name}")
     print(f"\tPlease try again\n")

#binary search --- take an ordered list and divide into 2 sections (high,low) and based on a middle point will continually halve the search pool until a unique value is found (or one isn't)
     
search_name = input("Enter the last name you are looking for")
min = 0
max = len(lname) -1

mid = int((min + max) / 2)
#this is for increasing (ascending) order
bin_count = 0
while (min < max and search_name != lname[mid]):
    bin_count += 1
     
    if search_name < lname[mid]:
          max = mid - 1

    else:
     min = mid + 1

    mid = int((min + max) /2)

    print(f"\n\tSearching Complete. Binary earch loop ran {bin_count} iterations.")

if search_name == lname[mid]:
     #found them! use 'guess' for index of found search item
     print(f"\t\t{fname[mid]} \t{lname[mid]} \t{fname[mid]} \t{id_stud[mid]} \t{class1[mid]} \t{class2[mid]} \t{class3[mid]}")

else:
    print(f"\n\tWe could not find {search_name}")
    print("Please try again.\n")

    #BUBBLE SORT----------------------------------------
nums = [100, 75, 32, 250, 47, 9, 2, 3, 99, 200]

print(f"Current List: {nums}")



for i in range(0, len(nums) -1):#outter loop

    print("OUTER LOOP! i = ", i)


    for index in range(0, len(nums) - 1):#inner loop

        print("\t INNER LOOP! k = ", index)

        #below if statement determines the sort

        #list used is the list being sorted

        # > is for increasing order, < for decreasing

        if(nums[index] > nums[index + 1]):

            print(f"\t\t SWAP! {nums[index]} <--> {nums[index + 1]}")

            #if above is true, swap places!

            temp = nums[index]

            nums[index] = nums[index + 1]

            nums[index + 1] = temp

print(f"Sorted List: {nums}")


        


