"""
⭐ Q5. Quiz Game
Create a function called quiz().
Ask 3 questions.
For each correct answer:
* Add 1 point.
At the end:
* Display total score.
* If score is 3, print "Excellent!"
* Otherwise print "Keep Practicing!"""

def quiz():
    total=0
    print("Which player has the most ODI centuries:\nA.Virat Kohli \n B.Sachin Tendulkar \nC. Don Bradman\n D.Ricky Ponting ")
    a1 = input(("Answer A,B,C or D: "))
    if a1.lower() == "a":
        print("Correct")
        total+=1
    else:
        print("Wrong")
    print("Which player has the most goals in World Cup finals: \nA.Pele\n B.Lionel Messi\nC.Cristiano Ronaldo\n D.Kylian Mbappe\nE.Zidane")
    a2 = input(("Answer A,B,C or D: "))
    if a2.lower() == "d":
        print("Correct")
        total+=1
    else:
        print("Wrong")
    print("Which was the largest non-colonial empire in history: \nA.British Empire\nB.Spanish Empire\nC. Mongol Empire\nD.Mughal Empire\nE.Abbasid Caliphate" )
    a3 = input(("Answer A,B,C or D: "))
    if a3.lower() == "c":
        print("Correct")
        total+=1 
    print(total) 
    if total==3:
        print("Excellent!")
    else:
        print("Keep practising")










quiz()