############          Q 1
str = input("Enter a string: ")
print("Number of characters:", len(str))
 

## Q 2
print(str.upper())
print(str.lower())

#### Q3

vcount = 0
for vowel in str:
    if vowel.lower() in "aeiou":
        vcount += 1

print("No. of vowels is:", (vcount))


## Q4

print (str[::-1])



### Q5

lower_count = 0
upper_count = 0

for i in str:
    if i.islower():
        lower_count += 1
    elif i.isupper():
        upper_count += 1

print("Lowercase letters:", lower_count)
print("Uppercase letters:", upper_count)

## Q6
c = input("Enter the character to count: ")

count = str.count(c)

print("It appears", count, "times.")



# Q7
words = str.split()

longest = ""

for word in words:
    if len(word) > len(longest):
        longest = word

print("Longest word:", longest)


# Q8
words = str.split()

print("Total number of words:", len(words))


# Q9
word = input("Enter a word: ")

if word[0].lower() in "aeiou":
    print("Starts with a vowel")
else:
    print("Starts with a consonant")


# Q10
words = str.split()

for word in words:
    if len(word) > 4:
        print(word)


# Q11
password = input("Enter a password: ")

has_number = False
has_uppercase = False

for ch in password:
    if ch.isdigit():
        has_number = True
    if ch.isupper():
        has_uppercase = True

if len(password) >= 8 and has_number and has_uppercase:
    print("Valid password")
else:
    print("Invalid password")


# Q12
letters = 0
digits = 0
spaces = 0

for ch in password:
    if ch.isalpha():
        letters += 1
    elif ch.isdigit():
        digits += 1
    elif ch == " ":
        spaces += 1

print("Letters:", letters)
print("Digits:", digits)
print("Spaces:", spaces)