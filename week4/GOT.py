#Latoya Hall
#2/7/2024

#----------------VARIABLE DICTIONARY------------------------------------

import csv

fname = []
lname = []
age = []
nname = []
alleg = []

#allegiances = ['Stark', 'Baratheon','Tully','Nights Watch', 'Lannister', 'Targaryen']
#mottos = ['Winter is Coming', 'Ours is the fury', 'Family. Duty. Honor.', 'And now my watch begins.', 'Hear Me Roar!', 'Fire and Blood']   

with open ("week4/files/lab4A_GOT_NEW.txt") as csvfile:

    file = csv.reader(csvfile)

    for rec in file:

        fname.append(rec[0])
        lname.append(rec[1])
        age.append(int(rec[2]))
        nname.append(rec[3])
        alleg.append(rec[4])


print(f"{'FIRST':12} \t {'LAST':12} \t {'AGE':3} \t {'NICKNAME':18} \t {'HOUSE':15}")
print("--------------------------------------------------------------------------------")

for i in range(0, len(fname)):

    print(f"{fname[i]:12} \t {lname[i]:12} \t {age[i]:3} \t {nname[i]:18} \t {alleg[i]:15}")


print(f"{'FIRST':12} \t {'LAST':12} \t {'AGE':3} \t {'NICKNAME':18} \t {'HOUSE':15} \t{'MOTTO':25}")
print("---------------------------------------------------------------------------------------------------")


for i in range(0, len(fname)):
    house = alleg[i]
    motto = ""
    

    if house == " House Stark":
        motto = "Winter is Coming"

    elif house == "House Baratheon":
        motto = "Ours is the fury"

    elif house == "House Tully":
        motto = "Family. Duty. Honor."

    elif house == "Night's Watch":
        motto = "And now my watch begins."

    elif house == "House Lannister":
        motto = "Hear Me Roar"

    else:
        house ="House Targaryen"
        motto = "Fire and Blood"

    


    print(f"{fname[i]:12} \t {lname[i]:12} \t {age[i]:3} \t {nname[i]:18} \t {alleg[i]:15} \t {motto:25}")

    

