#Latoya Hall
#week4_classlab.py

#VARIABLE DICTIONARY



#-------------------------------------------------------------


import csv

#create 1D lists [will be parallel to each other]
#base lists on fields in file

fname = []
lname = []
test1 = []
test2 = []
test3 = []

#connect to file and read data into 1D lists
with open("week4/files/week4_list.txt") as csvfile:

    file = csv.reader(csvfile)

    #come back and show print (file) later

    for rec in file:
        #store data from file fields to their respective lists
        #by parallel - storing initial file record data at the same position (index) in each list --> use the same [INDEX] across each list to find "matching" data

        fname.append(rec[0])
        lname.append(rec[1])
        test1.append(int(rec[2])) #cast test scores as integers for math
        test2.append(int(rec[3]))
        test3.append(int(rec[4]))
#disconnected from file----------------------------------------
print(f"{'FIRST':12} \t {'LAST':12} \t {'TEST1'} \t {'TEST2'} \t {'TEST3'}")
        
#process the lists --> for loop
for i in range(0,len(fname)):
    #len() --> returns length of (item) --> for lists, it is the # of items in the list

    print(f"{fname[i]:12} \t {lname[i]:12} \t {test1[i]} \t {test2[i]} \t {test3[i]}")
print("-----------------------------------------------------------------------------------")

#calculate and store each students average test score
avg = 0
total_count = 0
average = []

for i in range(0, len(test1)):

    #calculate avg for student
    avg = (test1[i] + test2[i] + test3[i]) /3 


    #append this avg to the avg[]
    average.append(avg)

# display students first name and average
    
print(f"{'FIRST NAME'}\t{'AVERAGE'}")
for i in range(0, len(fname)):
    print(f"{fname[i]:12} \t {average[i]:8.1f}") 

#SEQUENTIAL SEARCH: "in sequence" --> from beginning THROUGH the end
    
low_name = ""
low_avg = 100 #start with the highest value to drop to find the lowest

for i in range(0,len(average)):

    #determine if the curernt average is lower than current low_avg
    if average[i] < low_avg:
        low_avg = average[i] #current average is lower, so becomes new low value
        low_name = fname[i]

print(f"STUDENTS IN FILE: {len(fname)}")
print(f"LOWEST AVERAGE: {low_name} - {low_avg:.1f}")
#---2D LISTS--------------------------------------------------------------------------
#HINT: the 2D list is a list...populated with the lists 8D

all_students = []
for i in range(0, len(fname)):

    #add each students data to their (index) place in the all_students[]
    all_students.append([fname[i], lname[i], test1[i], test2[i], test3[i], average[i]])

    #display the 2D list to the console - for now, just get the lists to display ie ['Floyd', 'Eastham', '100', '85', '93']
for i in range(0,len(all_students)):
    print(f"{all_students[i]}")

print(f"{'FIRST':12} \t {'LAST':12} \t {'TEST1'} \t {'TEST2'} \t {'TEST3'} \t {'AVERAGE'}")
print("------------------------------------------------------------------------")

    #display the 2D list to the console where each value for each list appears as a value (and not a list item)
for i in range(0,len(all_students)):

    #inner for handles each value found at curent list (all_students[i])
    for x in range(0, len(all_students[i])):

        if type(all_students[i][x]) == str:
            print(f"{all_students[i][x]:12} ", end="")
            

        #inner for handles each value found at the current list (all_students[i])
        else:
            print(f"{all_students[i][x]:7.1f} ", end="")

    #include an extra empty print() to cancel the interior print's end = ""
    print()

#calculate average and letter grade
let_avg = []
avg = []

for i in range(0, len(all_students)):

    test_avg = (test1[i] + test2[i] + test3[i]) /3 
    avg.append(test_avg)
    
    if average[i] >= 90:
        let_a = "A"

    elif average[i] >= 80:
        let_a = "B"

    elif average[i] >= 70:
        let_a = "C"

    elif average[i] >= 60:
        let_a = "D"

    else:
        let_a = "F"

    let_avg.append(let_a)
  

print(f"{'FIRST':12} \t {'LAST':12} \t {'TEST1'} \t {'TEST2'} \t {'TEST3'} \t {'AVERAGE'} \t {'LETTER AVERAGE'}")
    for x in range(0, len(all_students)):
    
    
    print(f"{'LETTER AVERAGE: '}{let_avg[i]}")
