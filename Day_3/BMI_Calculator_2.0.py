height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))


BMI = (weight/(height**2))

RoundBMI = round(BMI)

if RoundBMI >= 35:
    print(f"Your BMI is {RoundBMI}, you are clinically obese.")

elif RoundBMI >= 30:
    print(f"Your BMI is {RoundBMI}, you are obese.")

elif RoundBMI >= 25:
    print(f"Your BMI is {RoundBMI}, you are slightly overweight.")

elif RoundBMI >= 18.5:
    print(f"Your BMI is {RoundBMI}, you have a normal weight.")

else:
    print(f"Your BMI is {RoundBMI}, you are underweight.")