#QUESTION 1
# (a) PSEUDOCODE
# INPUT radius
# SA = 4*pi*r**2
#V = (4/3)*pi*r**3
#OUTPUT Suface Area
#OUTPUT Volume

#(c)
import math
pi = math.pi

radius = int(input("Enter radius of sphere => "))

def calc(radius):
    SA = 4*pi*radius**2
    V = (4/3)*pi*radius**3
    return(SA, V)

SA, V = calc(radius)
print(f'''
Surface Area is : {SA}
Volume is : {V}
''')
# print(f'''
# Surface Area is : {calc(radius)[0]}
# Volume is : {calc(radius)[1]}
# ''')

#-----------------------------------------------------------------------------------------

#QUESTION 2
# age = int(input("Enter your age => "))

# if age >= 60:
#     print("You are a senior citizen")
# else:
#     print("You are not a senior citizen")