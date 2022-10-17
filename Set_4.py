# QUESTION 1
#  (a) PSEUDOCODE
# INPUT length of base
# INPUT height of parallelogram
# A = bh 
# OUTPUT = Area

# (c)
# b = int(input("Enter length of base of parallelogram => "))
# h = int(input("Enter height of parallelogram => "))

# def calcArea(b, h):
#     A = b*h
#     return A

# print(f"The area of the parallelogram is {calcArea(b, h)}")

#---------------------------------------------------------------------------------------------

#QUESTION 2
# age = int(input("Enter age => "))
# gender = str.upper(input("Enter your gender: M for Male and F for Female => "))
# num_days = int(input("Enter number of days worked => "))

# if age >= 18 and age < 30:
#     if gender == "M":
#         wage = 700*num_days
#         print(f"Your wage is {wage}")
#     elif gender == "F":
#         wage = 750*num_days
#         print(f"Your wage is {wage}")
#     else:
#         print("Enter aprropriate gender")
# elif age >= 30 and age <= 40:
#     if gender == "M":
#         wage = 800*num_days
#         print(f"Your wage is {wage}")
#     elif gender == "F":
#         wage = 850*num_days
#         print(f"Your wage is {wage}")
#     else:
#         print("Enter aprropriate gender")
# else:
#     print("Enter appropriate age")