#ORD
alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" 
for letter in alphabets:
    print(f"{letter}: {ord(letter)}")

print("/n+++++++++++++++++++/n")

alpha = alphabets.lower()

for char in alpha:
    print(f"{char} : {ord(char)}", end=", ")

    
    
    
    
#chr

print(chr(65,))
print(ord(" "))

letter = input("Enter a letter: ")
if letter.isalpha():
    if ord(letter) >=65 and ord(letter) <=90:
        print("It is a capital letter")
    else:
        print("It is a lowercase letter")
else:
    print("It is not a letter")