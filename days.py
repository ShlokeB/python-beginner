"""
You are tasked with writing a Python program that outputs a message based on the current day of the week. The program should follow these rules:
If the day is Monday, print "Start of the work week!".
If the day is Friday, print "Almost weekend!".
If the day is Saturday or Sunday, print "Weekend!".
 •  4. For any other day (Tuesday, Wednesday, Thursday), print "Just another weekday."
"""
day = input("Enter the day of the week:").lower()
if day == "monday":
    print("Start of the work week!")

elif day == "friday":
    print("Almost weekend!")

elif day == "saturday" or day =="sunday":
    print("Weekend!")

else :
    print ("Just another weekday.")