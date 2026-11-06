sentence = input("Enter a sentence: ")

alphabet = "abcdefghijklmnopqrstuvwxyz"
count = 0

for letter in alphabet:
    if letter in sentence.lower():
        count += 1

if count == 26:
    print("The sentence is a pangram")
else:
    print("The sentence is not a pangram")