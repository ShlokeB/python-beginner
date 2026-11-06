str = "A man a plan a canal Panama"

clean_str= str.replace (" ","").lower()

print(clean_str)

if clean_str== clean_str[::-1]:
    print("It is a palindrome")
else:
    print("It is not a palindrome")