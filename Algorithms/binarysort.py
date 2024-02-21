#Binary Search Algorithm:

search = input("Get search from user!")

min = 0

max = records - 1       #can also use len(listName) for 'records' value


guess = int((min + max) / 2)

#this is for INCREASING order ---this is the searching loop

while (min < max and search != listName[mid]):

   if search < listName[mid]:

       max = guess - 1

   else:

       min = guess + 1

   guess = int((min + max) / 2)

if search == listName[mid]:

    #found them! use 'mid' for index of found search item
    print()
else:

    #boooo not found
    print()