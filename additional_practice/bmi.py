#The body mass index (BMI) is used by health and nutrition professionals to quickly estimate body fat in certain populations.
#The formula is pretty simple: Take an individual's weight (mass) in kilograms and dividing it by their height in meters, squared.
import os 
os.system("cls")

mass = float(input("Enter mass in kg: "))
height = float(input("Enter height in m: "))

bmi = mass/(height**2)
bmi_rounded = round(bmi, 2)

print ("mass= ", mass, "kg")
print("height=", height, "m" )
print("bmi= ",bmi)
print("BMI= ", bmi_rounded)

if bmi < 18.5:
    print("underweight")

elif bmi >= 18.5 and bmi <= 24.9:
    print("Normal weight")

elif bmi >= 25 and bmi <= 29.9:
    print ("Overweight")

else:
    print("Obese")
    
