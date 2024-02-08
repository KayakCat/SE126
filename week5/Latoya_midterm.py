import csv

fname = []
bday = []
zodiac = []

with open ("week5/Latoya_midterm.txt") as csvfile:

    file = csv.reader(csvfile)

    for rec in file:
        fname.append(rec[0])
        bday.append(rec[1])
        zodiac.append(rec[2])

print(f"{'FIRST NAME':8} \t {'BIRTHDAY':5} \t {'ZODIAC SIGN':15}")
print("--------------------------------------------------------------------------------")

for i in range(0, len(fname)):

    print(f"{fname[i]:8} \t {bday[i]:5} \t\t {zodiac[i]:15}")


print(f"{'FIRST NAME':8} \t {'BIRTHDAY':5} \t {'ZODIAC SIGN':15} \t {'TAROT CARD':15}")
print("--------------------------------------------------------------------------------")

tarot_card = []

for i in range(0, len(fname)):

    if zodiac[i] == "Aries":
        tarot_card.append("The Emporer")

    elif zodiac[i] == "Taurus":
        tarot_card.append("The Hierophant")

    elif zodiac[i] == "Gemini":
        tarot_card.append("The Lovers")

    elif zodiac[i] == "Cancer":
        tarot_card.append("The Chariot")

    elif zodiac[i] == "Leo":
        tarot_card.append("The Sun")

    elif zodiac == "Virgo":
        tarot_card.append("The Hermit")

    elif zodiac == "Libra":
        tarot_card.append("Justice")

    elif zodiac == "Scorpio":
        tarot_card.append("Death")

    elif zodiac == "Sagittarius":
        tarot_card.append ("Temperance")

    elif zodiac == "Capricorn":
        tarot_card.append("The Devil")

    elif zodiac == "Aquarius":
        tarot_card.append("The Star")

    elif zodiac == "Pisces":
        tarot_card.append("The Moon")

    else:
        tarot_card.append("Invalid entry")


    print(f"{fname[i]:8} \t {bday[i]:5} \t\t {zodiac[i]:15} \t {tarot_card[i]:15}")





    





