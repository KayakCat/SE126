import csv

fname = []
bday = []
zodiac = []

with open ("week5/Latoya_Midterm.csv") as csvfile:

    file = csv.reader(csvfile)

    for rec in file:
        fname.append(rec[0])
        bday.append(rec[1])
        zodiac.append(rec[2])

print(f"{'FIRST NAME':8} \t {'BIRTHDAY':5} \t {'ZODIAC SIGN':15}")
print("--------------------------------------------------------------------------------")

for i in range(0, len(fname)):

    print(f"{fname[i]:8} \t {bday[i]:5} \t\t {zodiac[i]:15}")


#for i in range(0, len(fname)):

    





