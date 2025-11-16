
print("________TASK 1_________")
#program that asks the user for two numbers, a and b, and then calculates the hypotenuse c

import math 

side_a = float(input("Enter a of the triangle: "))
side_b = float (input("Enter b of the triangle: "))
side_c = math.sqrt(side_a**2 + side_b**2)

print ("The hypotenuse is: ", round(side_c, 2))


print("\n__________TASK 2___________")
#Write a program that asks the user to enter three numbers, and then calculates the solutions of the quadratic equation using the quadratic formula. 
# The program should print the discriminant and the real roots (if they exist).

a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

d = b**2 - 4*a*c

if d > 0:
    print ("Two real roots")

    x1 = (-b + math.sqrt(d)) / (2*a)
    x2 = (-b - math.sqrt(d)) / (2*a)
    
    print("x1 = ", round(x1, 2))
    print("x2 = ", round(x2, 2))

elif d == 0:
    print ("One real root")

    x = -b / (2*a)
    print("x =", round(x, 2))

else:
    print ("No real roots")
