#Latoya Hall
#latoya_midterm.py
#02/13/2024

#---------------VARIABLE DICTIONARY------------------------------------------------------
#fname                      first name in text file
#bday                       month and day of birth in text file
#zodiac                     zodiac sign in text file
#tarot_card=[]              used to assign tarot cards to each zodiac sign
#zodiac_traits = []         to assign traits to the zodiac signs
#tarot_card_info_upright    dictionary of all tarot cards and their upright meanings
#tarot_card_info_reversed   dictionary of all tarot cards and their reversed meanings
#def get_tarot_card_meaning function created to be able to use the menu created to look up tarot card meanings in upright and reverse
#card                       parameter in the def get_tarot_card_meaning function to choose a tarot card
#orientation                parameter in the def get_tarot_card meaning function to choose upright or reversed orientation of tarot card
#meanings_dict              value used to assign orientation and card parameters in def get_tarot_meanings function
#meaning                    value assigned to else statement in the def get_tarot_card_meaning function for the card parameter and the return statment to exit the function
#def tarot_menu             menu created to search up tarot card meanings in upright and reverse
#choice                     variable assigned to create input statements for users to make selections in the menu
#-------------------Program Description----------------------------------------------------------------
#This program prints out a list of names, birthdays, and zodiac signs. It then prints out a second list that adds zodiac traits and the tarot card associated with the zodiac sign. After that a 4 choice menu pops up to look up the tarot card meanings in the upright and reversed positions

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
    #first list print
    print(f"{fname[i]:8} \t {bday[i]:5} \t\t {zodiac[i]:15}")


print(f"{'FIRST NAME':8} \t {'BIRTHDAY':5} \t {'ZODIAC SIGN':15} \t {'ZODIAC TRAITS':45} \t {'TAROT CARD':15}")
print("--------------------------------------------------------------------------------------------------------------------")

tarot_card = []#getting zodiac signs to assign tarot cards to each one
zodiac_traits = []

for i in range(0, len(fname)):

    if zodiac[i] == "Aries":
        tarot_card.append("The Emporer")
        zodiac_traits.append("Courageous, confident, and determined.")

    elif zodiac[i] == "Taurus":
        tarot_card.append("The Hierophant")
        zodiac_traits.append("Patient, reliable, and practical")

    elif zodiac[i] == "Gemini":
        tarot_card.append("The Lovers")
        zodiac_traits.append("Adaptable, outgoing, and intelligent")

    elif zodiac[i] == "Cancer":
        tarot_card.append("The Chariot")
        zodiac_traits.append("Emotional, intuitive, and protective")

    elif zodiac[i] == "Leo":
        tarot_card.append("The Sun")
        zodiac_traits.append("Confident, generous, and charismatic")

    elif zodiac[i] == "Virgo":
        tarot_card.append("The Hermit")
        zodiac_traits.append("Detail-oriented, practical, and analytical")

    elif zodiac[i] == "Libra":
        tarot_card.append("Justice")
        zodiac_traits.append("Charming, diplomatic, and fair-minded")

    elif zodiac[i] == "Scorpio":
        tarot_card.append("Death")
        zodiac_traits.append("Passionate, resourceful, and determined")

    elif zodiac[i] == "Sagittarius":
        tarot_card.append ("Temperance")
        zodiac_traits.append("Optomistic, adventurous, and independent")

    elif zodiac[i] == "Capricorn":
        tarot_card.append("The Devil")
        zodiac_traits.append("Ambitious, disciplined, and patient")

    elif zodiac[i] == "Aquarius":
        tarot_card.append("The Star")
        zodiac_traits.append("Inventive, open-minded, and humanitarian")

    elif zodiac[i] == "Pisces":
        tarot_card.append("The Moon")
        zodiac_traits.append("Compassionate, artistic, and intuitive")

    else:
        tarot_card.append("Invalid entry")
        zodiac_traits.append("N/A")

    #second list print
    print(f"{fname[i]:8} \t {bday[i]:5} \t\t {zodiac[i]:15} \t {zodiac_traits[i]:45} \t {tarot_card[i]:15}")

#Big dictionary of upright and reversed tarot card meanings
tarot_card_info_upright = {
    'The Emporer': "Do not let anyone else take your power away from you. Be a leader but not a dictator, find a balance between authority and compassion.",
    'The Hierophant': "You're the kind of person who sticks to the old-school way of doing things. Knowledge Sharing and Education: Sharing what you know with others is a big deal. Marriage and Teamwork: You like working with others and following the rules.",
    'The Lovers': "Represents choices, partnerships, and the union of opposites. It often signifies a significant decision that needs to be made, and it can indicate harmony and balance in relationships.",
    'The Chariot': "represents determination, success, and control. When it appears upright, it signifies that you're on the right path and should persevere in your endeavours.",
    'The Sun': "It is said to reflect happiness and contentment, vitality, self-confidence and success. Sometimes referred to as the best card in tarot, it represents good things and positive outcomes to current struggles.",
    'The Hermit': "the Hermit card encourages us to take a break, reflect on our lives, and understand ourselves better. It advises us to strike a balance between solitude and social interaction, and it reminds us that taking care of our mental and emotional well-being is essential.",
    'Justice': "represents justice, fairness, truth and the law. You are being called to account for your actions and will be judged accordingly.",
    'Death': "The Death tarot card is often misunderstood and feared, primarily due to its name. However, in the upright position, this card signifies not physical death but rather a profound transformation. It represents the end of a significant phase in your life that you recognize is no longer serving you.",
    'Temperance': "the Temperance card embodies a sense of balance, harmony, and patience. It signifies that your life is flowing smoothly and you've achieved inner peace. This card encourages you to maintain your composure, especially in challenging situations, and keep your emotions in check.",
    'The Devil': "The Devil tarot card suggests feelings of obsession, addiction, and entrapment. It can signify a sense of helplessness due to external forces or circumstances. However, it reminds you that you're responsible for your actions, and your perceived constraints are often self-imposed.",
    'The Star': "It signifies a renewal of spirit, bringing forth calmness, serenity, and an optimistic outlook for the future. This card represents a strong connection to one's spirituality and the potential for emotional and physical healing. It's a symbol of radiant, positive energy.",
    'The Moon': "The Moon represents your fears and illusions and often comes out when you are projecting fear into your present and your future, based on your past experiences."
}

tarot_card_info_reversed = {
    'The Emporer': "In the reversed position, The Emperor can be domineering and rigid in his thinking. The card can suggest an over-use and abuse of authoritative power surrounding you. It could originate from you or from another person, often a boss, partner or father figure. And it may be because of deep insecurities or father issues from childhood.",
    'The Hierophant': "All the wisdom you seek comes from within not from some external source or power. You are being guided to follow your own path and adopt your own spiritual belief systems rather than blindly following others. It may feel unsettling at first as you make your own way, but over time, you will learn to trust yourself and tap into your inner knowledge. ",
    'The Lovers': "Reversed, it can signal a time when you’re out of sync with those around you, particularly your loved ones. You may find your relationships are strained and communication is challenging. Does it seem as if you are just not on the same page and no longer share the same values? If so, come back to the reason you have this person in your life. If you love him or her unconditionally, know this moment shall pass and the best you can do is bring love and compassion to the situation. In other cases, you may realise that you have simply grown apart and it’s time to move on. If your relationship continues to be peppered by arguments and a lack of respect for one another, then it could be time to let go. Honour yourself and do what is best for you both.",
    'The Chariot': "Reversed, however, The Chariot tells you to ‘back up the truck’ or “do a U-turn”. You might bang your head against a brick wall, trying to push a project forward when really, you ought to back off or change direction. Or you might have lost your motivation and no longer feel as committed to the outcome as you did when you started. So, if something is not moving forward as you planned, re-evaluate the situation and check in to see if it’s a sign that you need to change course. ",
    'The Sun': "The Sun Reversed is calling to your inner child to come out and play! As adults, we get so lost in the hustle and bustle of everyday life that we forget how to have fun. But spend just a few minutes watching a kid play, and you realize how wonderful and carefree life can be when you learn to let go of your worries and concerns. When you see The Sun Reversed in your Tarot reading, see it as your permission slip to leave behind your work and responsibilities, even just for a moment, and play. Dance like no-one is watching, sing like no-one is listening, and let your heart and soul fly free.",
    'The Hermit': "The Hermit Reversed can go one of two ways: you are not taking enough time for personal reflection, or you are taking too much. If you struggle to connect with your spiritual self, The Hermit Reversed encourages you to create more space to meditate and reflect. It is time to go deeper into your inner being and rediscover your greater purpose on this earth. You may have been so busy dealing with the day-to-day issues that you have forgotten to listen to your inner voice. The Hermit asks you to search deep within your soul to help you find your way again and focus on rebuilding yourself on a spiritual level.",
    'Justice': "you are morally aware that what you did was wrong. You have two choices: hide it and hope no one finds out, or face your mistakes and take decisive action to correct the problem. ",
    'Death': "you are about to go through a significant transformation but are rejecting it. You could find it challenging to let go, or you might need help with how to implement the necessary adjustment. You still hold negative perspectives from history that might obstruct a fresh chance.",
    'Temperance': "Temperance Reversed can also be a sign you sense that something is off in your life, creating stress and tension. Life is not flowing as easily as you had hoped or theres a niggling voice from within going, “Wait a second! This doesnt feel right!” You can ignore it and carry on with life as usual. But, heed Temperances warning: If you stay in this state for too long, that voice will just get louder and louder until you pay attention. Or, you can listen to it now and make the necessary adjustments to find your flow once again. Focus on your long-term vision and higher purpose and seek to align your daily activities with this vision.",
    'The Devil': "The Devil Reversed can often appear when you are on the verge of a break-through or an up-levelling. You are being called to your highest potential, but first, you must let go of any unhealthy attachments or limiting beliefs that may hold you back. Often, when you are called to something ‘more’, you must deal with your shadows before you can step into this new version of yourself. It may be an addiction, unhealthy relationships, or a disengaging career. Let go of fear and release any self-imposed limiting beliefs standing in the way of your growth. It is easier than you realize.",
    'The Star': "The Star Reversed can mean that you’ve lost faith and hope in the Universe. You may be feeling overwhelmed by life’s challenges right now and questioning why you are being put through this. You know life throws curveballs, but really? Why this, and why now?! You may be desperately calling out to the Universe to give you some reprieve but struggling to see how the Divine is on your side. Look harder, and you will see it. The Divine is always there. Take a moment to ask yourself what the deeper life lesson is, and how this is a blessing, not a punishment.",
    'The Moon': "The Moon Reversed indicates that you have been dealing with illusion, fears, and anxiety, and now the negative influences of these energies are subsiding. You are working through your fears and anxieties, understanding the impact they have on your life and how you can free yourself from such limiting beliefs. This is a truly liberating and transformational experience."
}

def get_tarot_card_meaning(card, orientation='upright'):
    # Determine which dictionary to use based on the orientation of the tarot card using 2 parameters --> card and orientation  
    if orientation == 'upright':
        meanings_dict = tarot_card_info_upright
    else:
        meanings_dict = tarot_card_info_reversed

    # Retrieve the meaning using if else statements
    
    if card in meanings_dict:
        meaning = meanings_dict[card]
    else:
        meaning = f"Meaning for {card} not available for {orientation} orientation."

    return meaning    

#tarot menu to choose the card and orientation that you want the meaning of

def tarot_menu():
    print("\n--Tarot Card Meaning Lookup--")
    print("1. Upright Meaning")
    print("2. Reversed Meaning")
    print("3. What is the meaning of life")
    print("4. Exit")

    # Get the user's input (choice) to navigate the menu
    choice = input("Enter your choice (1, 2, 3, or 4): ")

    # Loop to trap the user if they don't follow the directions
    while choice not in ['1', '2', '3', '4']:
        print("*INVALID ENTRY* Enter 1, 2, 3, or 4 only.")
        choice = input("Enter your choice (1, 2, 3, or 4): ")

    return choice

choice = '0'

while choice != '4':

    choice = tarot_menu() #calling the menu into the loop

    if choice == '1':
        card = input("Enter the tarot card for upright meaning: ")
        meaning = get_tarot_card_meaning(card, 'upright')
        print(f"\nMeaning of {card} in the upright position: {meaning}")

    elif choice == '2':
        card = input("Enter the tarot card for reversed meaning: ")
        meaning = get_tarot_card_meaning(card, 'reversed')
        print(f"\nMeaning of {card} in the reversed position: {meaning}")

    elif choice == '3':
        print(f"42") #Hitchhikers Guide to the Galaxy Reference

    elif choice == '4':
        print("Exiting Tarot Card Meaning Lookup. Enjoy the magic of life. Marvel in the mysteries of the universe. Eat your vegetables...yum yum! Namaste!")






    





