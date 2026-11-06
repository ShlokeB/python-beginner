# Ask user to enter sentence and convert into all caps with ord and chr

sentence = input("Enter a sentence")
result = ""
for char in sentence:
    val = ord(char)
    if val >= 97 and val <= 122:
        result = result + chr(val - 32)
    else:
        result = result + char
print(result)