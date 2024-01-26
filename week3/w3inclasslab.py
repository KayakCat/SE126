#Latoya Hall
#1/23/2024
#w3inclass.py 
#Variable Dictionary

#total_records          total records in csv file
#rec                    a single record in the file
#comp_type              specifies if the computer is a desktop or laptop 
#manu                   specifies the manufacturer of the computer (dell, gateway, or HP) 
#processor              specifies the processor (i5 or i7)
#ram                    specifies the ram (8GB or 16GB)
#hdd_1                  specifies hard drive space (500GB or 001TB)
#num_hdd                specifies the number of hard drives (1 or 2)
#hdd_2                  if the computer has 2 hard drives this specifies space (500GB OR 001TB)
#os                     specifies the operating system 
#year                   specifies the year the computer was manufactured (range of 2015 - 2018) 
#file                   csv file
#desktop_count          number of desktops manufactured in 2016 or older
#laptop_count           number of laptops manufactured in 2016 or older
#desktop_count_cost     cost of desktops to be replaced (desktop_count * 2000)
#laptop_count_cost      cost of laptops to be replaced (laptop_count * 1500)
#-----------------------------------------------------------------------

import csv

#total counter for all records
total_records = 0

#create some lists - one for EACH potential field in file
comp_type_list =[]
manu_list =[]
processor_list = []
ram_list = []
hdd_1_list = []
num_hdd_list = []
hdd_2_list = []
os_list = []
year_list = []

print(f"{'TYPE':8} {'MANU':8} {'PROC':6} {'RAM':6} {'HDD 1':6} {'#HDD':5} {'HDD 2':6} {'OS':4} {'YEAR':4}")
print("------------------------------------------------------------------------------")

with open("lab2b.csv") as csvfile:

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

        #append respective values to the appropriate field list
        comp_type_list.append(comp_type)
        manu_list.append(manu)
        processor_list.append(processor)
        ram_list.append(ram)
        hdd_1_list.append(hdd_1)
        num_hdd_list.append(num_hdd)
        hdd_2_list.append(hdd_2)
        os_list.append(os)
        year_list.append(year)

        #final print for each record
        print(f"{comp_type:8} {manu:8} {processor:6} {ram:6} {hdd_1:6} {num_hdd:5} {hdd_2:6} {os:4} {year:4}")

 #----------DISCONNECTED FROM FILE--------------------------------  
print("-----------------------------------------------------------------")
print(f"TOTAL RECORDS: {total_records}")   

#process the lists to: print the machine data
for index in range(0, total_records):
    #for index in range(0, len(comp_type_list)): --> len(comp_type_list) returns the INTEGER count of values
    print(f"{comp_type_list[index]:8} {manu_list[index]:8} {processor_list[index]:6} {ram_list[index]:6} {hdd_1_list[index]:6} {num_hdd_list[index]:5} {hdd_2_list[index]:6} {os_list[index]:4} {year_list[index]:4}")

    #process the lists to: count the number of desktops

desktop_count = 0
laptop_count = 0
for index in range(0, len(comp_type_list)):
    #look through the comp type list to find "desktop"
    if comp_type_list[index] == "Desktop" and int(year_list[index]) <= 16:
            desktop_count += 1 #adds one for everytime "Desktop" 2016 or older is found

    elif comp_type_list[index] == "Laptop" and int(year_list[index]) <= 16:
        laptop_count += 1 #adds one for everytime a laptop 2016 or older is found

print(f"TOTAL DESKTOPS 2016 AND OLDER: {desktop_count}")  
print(f"TOTAL LAPTOPS 2016 AND OLDER:  {laptop_count}")      


            
desktop_count_cost = desktop_count * 2000 #calculate the cost to replace desktops 2016 and older

laptop_count_cost = laptop_count * 1500 #calculate the cost to replace laptops 2016 and older

print(f"To replace 8 Desktop computers it will cost: ${desktop_count_cost}")
print(f"To replace 2 Laptops it will cost:           ${laptop_count_cost}")
            


