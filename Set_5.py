# QUESTION 1
#  (a) PSEUDOCODE
# INPUT radius
# INPUT height
# Volume = pi*r**2*h
# Surface Area = 2*pi*r**2 + 2*pi*r*h
# OUTPUT Volume
# OUTPUT Surface Area

# (c)
# import math
# pi = math.pi 

# height = int(input("Height of cylinder = "))
# radius = int(input("Radius of cylinder = "))

# def calc(height, radius):
#     volume = pi*radius**2*height
#     surface_area = 2*pi*radius**2 + 2*pi*radius*height
#     return (volume, surface_area)

# print(f'''
# Volume is : {calc(height, radius)[0]}
# Surface Area is : {calc(height, radius)[1]}
# ''')

# --------------------------------------------------------------------------------------------

# QUESTION 2
# num = int(input("Enter a number => "))

# if num % 2 == 0 and num % 3 == 0:
#     print(f"{num} is divisable by 2 and 3")
# else:
#     print(f"{num} is not divisable by 2 and 3")