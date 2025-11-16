#Create a temperature.py program that converts a number from Celsius (°C) to Fahrenheit (°F)
#Use the current temperature of Sofia, Bulgaria.
#Formula: °F = °C * 1.8 + 32
import os 
os.system("cls")
Celsius = float(input("Enter temperature in Celsius: "))
Fahrenheit = Celsius * 1.8 + 32
print("Celsius = ", Celsius)
print("Fahrenheit = ", Fahrenheit)
