# Area Calculator

print("~~~~~~~~~~~~~~~~")
print("Area Calculator")
print("~~~~~~~~~~~~~~~~")
print('\n')
print("1. Triangle")
print("2. Rectangle")
print("3. Square")
print("4. Circle")
print("5. Quit")
print('\n')

user_input = int(input("Which shape: "))

base = int(input("Base: "))
height = int(input("Height: "))

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
else:    print("Invalid input. Please select a number between 1 and 5.")
