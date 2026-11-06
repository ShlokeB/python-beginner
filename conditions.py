weight = float(input("Enter the weight in kg: "))
height = float(input("Enter the height in m: "))
bmi = weight/(height**2)
print(f"The BMI is: {bmi:.2f}")

if bmi<=18.5:
    print("You are underweight")
elif bmi > 18.5 and bmi <=24.9:
    print("You are healthy")
elif bmi >=25 and bmi <=29.9:
    print("You are overweight")
elif bmi >=30 and bmi <= 34.9:
    print("You are obese")
elif bmi >=35 :
    print("You are extremeley obese")
    