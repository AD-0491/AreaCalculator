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

print(f"The area is {}")