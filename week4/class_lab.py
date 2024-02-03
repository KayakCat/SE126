#Latoya Hall
#2/3/2024

#I want to be a great python programmer, I spend so many hours working on it and confused...I get it done, but it is a feat. Python is my kryptonite. ONE DAY I WILL PREVAIL!!!
#-------------------VARIABLE DICTIONARY------------------------
#fname              first name of student in record
#lname              last name of student in record
#test1              first test score
#test2              second test score
#test3              third test score
#grades             the variable assigned to the csv file
#average = []       used to pull the average from the records
#avg                (test1[i] + test2[i] + test3[i]) /3
#class_avg          sum(average) / len(average)
#all_students = []  used to make 2D list aka !!!!!!INCEPTION!!!!!
#let_avg = []       used to pull average from records to determine letter grades in else/if for loop                     
#let_a              variable used to assign letter grades 
#-----------------MAIN PROGRAM------------------------------------

import csv

#create 1D list based on fields in the file
fname = []
lname = []
test1 = []
test2 = []
test3 = []

#connect to the file and read the data into 1D lists
with open ("week4/files/week4_list.txt") as file:
    grades = csv.reader(file)

    for rec in grades:
        #store data from file fields to their respective lists
        #by parallel - storing intial file record data at the same position (index) in each list --> use the same [index] across each list to find matching data

        fname.append(rec[0])
        lname.append(rec[1])
        test1.append(int(rec[2]))
        test2.append(int(rec[3]))
        test3.append(int(rec[4]))
#disconnect from file--------------------------------------------------------------
print(f"{'FIRST NAME':12} \t {'LAST NAME:':12} \t {'TEST 1':12} \t {'TEST 2':12} \t {'TEST 3':12}")

#process the lists --> for loop
for i in range(0,len(fname)):
    #len() --> returns length of (item) --> for lists, it is the # of items in the list

    print(f"{fname[i]:12} \t {lname[i]:12} \t {test1[i]:3} \t {test2[i]:10} \t {test3[i]:10}")
print("---------------------------------------------------------------------------------------------------------------------------------------------")

#initialize variables to store each students average score
avg = 0
average = []

for i in range(0, len(test1)):
    #calculate avg for students
    avg = (test1[i] + test2[i] + test3[i]) /3

    #append the avg (what was calculated above) to the average[]
    average.append(avg)

    #display students first name and average
print(f"{'FIRST NAME'}\t{'AVERAGE'}")

for i in range(0, len(fname)):
    
    print(f"{fname[i]:12} \t {average[i]:4.1f}")
print("----------------------------------------------------------------------------------------------------------------------------------------")

for i in range(0,len(average)):

    class_avg = sum(average) / len(average) #MATH :( LOLOL MY BRAIN IS FRIED
    #ANYWAY sum(average) / len(average) calculates the sum of all the values in average and divides by the number of students in the average list

print(f"STUDENTS IN FILE: {len(fname)}") 
print(f"Class Average: {class_avg:4.1f}")

print("-----------------------------------------------------------------------------------------------------------------------------------------")



#-----2D lists----------------------------------
all_students = []
for i in range(0,len(fname)):
    #add each students data to their (index) place in all_students[]
    all_students.append([fname[i], lname[i], test1[i], test2[i], test3[i], average[i]])

     


let_avg = []

for i in range(0, len(average)): #for loop with else/if statements to filter grade averages into letter grades
    
    
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

    let_avg.append(let_a) #add each letter grade to the students record
  

print(f"{'FIRST':12} \t {'LAST':12} \t {'TEST1':12} \t {'TEST2':12} \t {'TEST3':12} \t {'AVERAGE':8} \t {'LETTER GRADE':12}")

for i in range(0,len(all_students)):
    
    
    
    print(f"{fname[i]:12} \t {lname[i]:12} \t {test1[i]:3} \t {test2[i]:10} \t {test3[i]:10} \t {average[i]:13.1f} \t\t  {let_avg[i]:12}") #final print statement with letter grade included with everything else that was printed previously

    #this took me like 8 hours total to do...how can i get faster....
    #ahdsfjhdanfjieniavjbeqawvlibrsmvndnjfnsajkfnjdknjkfdsnfjkndjkfjkadbnfjakvjkalbdjvbkaljdfndajkfndjsakfkdsfnjksdfanjkdsanfvjkbvhjafkd vjksanvjlsak;nkjsl;nksnfkldnavkldnvjkfvbsjkvbdjkbvajksdvjkdasbnvjkdsnvjkabnsvjka.....this is my brain

    












