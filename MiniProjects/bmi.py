weight=float(input("enter your weight in kg:"))
height=float(input("enter your height in m:"))
BMI=weight/height**2
if BMI < 18.5:
    print("under weight")
elif BMI < 25:
    print("healthy weight")
else:
    print("over weight")