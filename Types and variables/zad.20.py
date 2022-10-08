print("Calculate your BMI")

print("Enter your height in cm: ")
x=int(input())
print("Enter your weight in kg: ")
y=int(input())

bmi=(y/(x**2))*10000
f_bmi="{:.2f}".format(bmi)

print(f"BMI index: {f_bmi}")