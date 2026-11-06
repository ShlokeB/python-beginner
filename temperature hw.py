temperature = float(input("Enter the temperature in Celsius: "))

if temperature < 0:
    print("Freezing Cold! Stay indoors.")

elif temperature <= 10:
    print("Very Cold! Wear heavy winter clothing.")

elif temperature <= 20:
    print("Cool. A light jacket will do.")

elif temperature <= 30:
    print("Pleasant weather. Enjoy!")

else:
    print("Hot! Stay hydrated.")