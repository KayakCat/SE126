#Latoya Hall
#1/23/2024
#hw_week2.py 

#Variable Dictionary
#total_records        total counter for all records
#file                 variable for the csv file
#comp_type            specifies if its a laptop or desktop
#manu                 specifies the manufacturer of the computer hp, dell, gateway
#ram                  specifies GB of Ram - 8 or 16
#hdd_1                specifies the amount of space on the first hardrive (001TB or 500GB)
#num_hdd              number of hard drives the computer has
#hdd_2                specifies the amount of space on the second hard drive if they have one(001TB or 500GB)
#os                   the version of windows the system has installed
#year                 manufacture date of computer
#-----------------------------------------------------------------------

import csv

#total counter for all records
total_records = 0

print(f"{'TYPE':8} {'MANU':8} {'PROC':6} {'RAM':6} {'HDD 1':6} {'#HDD':5} {'HDD 2':6} {'OS':4} {'YEAR':4}")
print("------------------------------------------------------------------------------")

with open("week3/lab2b.csv") as csvfile:

    file = csv.reader(csvfile)

    for rec in file:

        #print(rec) #shows as a list -> []

        #keep track of the rec count in the file
        total_records += 1 #total_records = total_records + 1

        #filter for display------------------------------------------------

        if rec[0] == "D":
            comp_type = "Desktop"
        elif rec[0] =="L":
            comp_type = "Laptop"
        else:
            comp_type = "ERROR" +str(rec[0])

        #storing value for var representing field 2 "manu" (rec[1])
        #---------------------------------------------------
        
        if rec[1] == "DL":
            manu = "Dell"
        elif rec[1] == "GW":
            manu = "Gateway"
        elif rec[1] == "HP":
            manu = rec[1]
        else:
            manu = "ERROR" +str(rec[1])
        
        #---storing value for vars representing field3, field4, field5, & field6 (no filtering necessary) rec[2], rec[3], rec[4], rec[5]
            
        processor = rec[2]
        ram = rec[3]
        hdd_1 = rec[4]
        num_hdd = rec[5]

        if rec[5] == "1":
            hdd_2 = " " #"---" #"none"
            os = rec[6]
            year = rec[7]
        elif rec[5] == "2":
            hdd_2 = rec[6]
            os = rec[7]
            year = rec[8]

        else:
            hdd_2 = "ERROR" +str(rec[5])
            os = "ERROR"
            year = "ERROR"

        print(f"{comp_type:8} {manu:8} {processor:6} {ram:6} {hdd_1:6} {num_hdd:5} {hdd_2:6} {os:4} {year:4}")

 #----------DISCONNECTED FROM FILE--------------------------------  
print(f"TOTAL RECORDS: {total_records}")             



