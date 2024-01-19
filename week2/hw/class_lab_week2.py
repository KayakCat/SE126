#Latoya Hall
#January 19, 2024
#Class_lab_week2.py


#-----------VARIABLE DICTIONARY------------------------------------------------------

# max_capacity          maximum number of people allowed in the room
# people_registered     number of people registered for the meeting
# rooms_over_limit      rooms that have more people registered than the maximum capacity
# rooms                 meeting rooms 
# people_notified       people notified that they are on a waitlist for a meeting that is over capacity
# records_processed     each room that is checked for capacity limits is a record processed

#-------------------------------------------------------------------------------------

#import csv file for text file handling functions
import csv

#initialize counting variables - counts from file
records_processed = 0
rooms_over_limit = 0
people_notified = 0

#initialize empty lists - 1 list per field

room_name = [] #name of the meeting room
room_capacity = [] #maximum capacity of the room
registered = [] #number of people registered for the meeting

#connect to the file
with open("week2/hw/lab2a.csv") as unicorn:
    file = csv.reader(unicorn)

#go in and "read" each record in the file
    for rec in file:
        #for every record in found in the file (entire row of field data)

        #display data in neat columns
        print(f"{rec[0]:15} \t{rec[1]:10} \t{rec[2]:10}")

        #store data from the rec list (current record being read) to list
        #adding data to a  list --> .append(); requires list name as starting object 
        room_name.append(rec[0]) 
        room_capacity.append(int(rec[1]))
        registered.append(int(rec[2]))

        #keep literal count of number of records
        records_processed += 1

    for rec in file:
    
        if (int(rec[2])) > (int(rec[1])):

            rooms_over_limit += 1

            people_notified = (int(rec[2])) - (int(rec[1]))

print(f"Total Records Processed: {records_processed}")
print(f"Total Rooms Over Capacity: {rooms_over_limit}")
print(f"Total People to be Notified: {people_notified}")









                            













