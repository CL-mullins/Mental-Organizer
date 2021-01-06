import pandas as pd
import random

#Takes string from user
query1 = input("What would you like to do?: ")





#String is then used to evaluate importance of task.

#These will be the top 3 topics that I tend to search for when I am studying x subject.
topic1 = 'null'
topic2 = 'null'
topic3 = 'null'

#This will be the top value or the average value for what my mood is for when I tell the program that I am
#nervous
moodTranslation = "excited"
moodEffects = ["frazzled", "distractable", "unfocused"]

if "idk" or "i don't know" or "i dont know" in query1:
    query1_2 = input("How are you feeling?: ")
    if "antsy" or "run" or "walk" in query1_2:
        print("You're probably feeling nervous.")
        query1_3 = input("Would you like for me to recommend some ways to relieve your nervousness?: ")
        if "yes" or "sure" or "please" in query1_3:
            mood = 'nervous'
            #TODO: Make this into it's own function
            print(f"Well, to make things short, when you're {mood}, typically you're {moodTranslation}.")
            print(f"When you're {moodTranslation}, your mind tends to be {moodEffects[random.randint(0,2)]}")

if "read" in query1:
    pass

#Example query where I want to study
if "study" in query1:
    query1_1 = input("What are you going to study?: ")
    if "CS" or "Computer Science" or "Programming" or "programming" in query1_1:
        query1_2 = input("That's a little bit too broad, what are you focusing on?: ")
        if "idk" or "i don't know" in query1_2:
            print(f"Well, you typically study {topic1}, {topic2}, and {topic3}, are those it?")
            query1_3 = ("or would you like to study something else?: ")


#Topics can be determined by prior use. Prior use needs to be stored in some database, perhaps a CSV file 
#could be made to store data
#Top topics are determined by number of entries of that topic into the study spreadsheet.

#Example query where I say I want to run
if "run" in query1:
    query1_1 = input("How are you feeling?: ")
    if "good" or "excited" in query1_1:
       query1_2 = input("Meditate for five minutes first, then go. OK?: ")
       if "OK" or "Okay" or "ok" or "o.k" in query1_2:
           query1_3 = input("I'll set a timer for five minutes, would you like to start now?: ")
           if "yes" or "sure" or "fine" or "YES" or "Yes" in query1_3:
               #start timer
               exit


#Terminates on close, or terminate, or end

importance = 0
#"Need" is half as important as "want"
#if query contains "need" importance + 5 if query contains "want": importance + 2.5
#If it contains both queries, separate it based on a comma:
#Example: "I need to do this, but I want to do this"
#Address the 'need' first as if it were it's own query, but don't forget to address the 'want'