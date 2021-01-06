
#Takes string from user
query1 = input("What would you like to do?: ")

#String is then used to evaluate importance of task.

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