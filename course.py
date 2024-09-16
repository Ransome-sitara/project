#!/usr/bin/env python3
#weight converte

year_of_birth = input ("year of birth: ")
age = 2024 -   int(year_of_birth)
print (age)
name = input ("name: ")
weight = int(input("weight: "))
unit = input("(l)bs  or (k)s:")
if unit.upper == "L":
     converted =  weight * 0.45
     print (f"{name} you are {age} years old and you weigh {converted} killos")
else:
         converted = weight / 0.45
         print (f"{name} you are {age} years old and you weigh {converted} pounds") 
