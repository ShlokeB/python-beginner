sentence= input("Enter a sentence: ")
for letter in sentence:
    if letter.isalpha():
        x = ord(letter)
        x+=1
        print(chr(x), end="")
    else: print(letter, end = "")