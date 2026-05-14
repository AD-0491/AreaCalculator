# Area Calculator
import time 

time.sleep(0.2)
print("~~~~~~~~~~~~~~~~~~~")
print("| Area Calculator |")
print("~~~~~~~~~~~~~~~~~~~")

time.sleep(1)
print("1. Triangle")
time.sleep(1)
print("2. Rectangle")
time.sleep(1)
print("3. Square")
time.sleep(1)
print("4. Circle")
time.sleep(1)
print("5. Quit")
time.sleep(1)
print()

user_input = int(input("Pick a shape: "))
print()
base = int(input("Base: "))
height = int(input("Height: "))
print()

triangle_area = (height * base) / 2
rectangle_area = height * base
square_area = height * height
circle_area = 3.14 * (height ** 2)

if user_input == 1:
    print(f"Area of Triangle: {triangle_area}")
elif user_input == 2:
    print(f"Area of Rectangle: {rectangle_area}")
elif user_input == 3:
    print(f"Area of Square: {square_area}")
elif user_input == 4:
    print(f"Area of Circle: {circle_area}")
elif user_input == 5:
    print("Goodbye!")
else:    
    print("Invalid input. Please select a number between 1 and 5.")
