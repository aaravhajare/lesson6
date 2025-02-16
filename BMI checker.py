weight = float(input("enter you weight"))
height = float(input("enter your height"))

bmi =  weight / (height/100)**2

print(f"your BMI is {bmi}")

if bmi <= 18.4 :
    print("you are under weight")

elif bmi <= 24.9:
    print("you are healthy")

elif bmi <= 29.9:
    print("you are over weight")

elif bmi <= 34.9:
    print("you are severly over weight")

elif bmi <= 39.9:
    print("tou are severly obese ")