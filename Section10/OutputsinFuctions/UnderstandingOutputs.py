# Pruebas de Output Functions
import re

def suma():
    result = 3*2
    return result #the function will be now result


def und_input(name_1, name_2): #use parentesis to call variables
    print(name_1.title())
    print(name_2.title())
    
def und_input_2(name_1, name_2): #use parentesis to call variables
    formated_name_1 = name_1.title()
    formated_name_2 = name_2.title()
    return f"{formated_name_1} {formated_name_2}"

extra_variable = und_input_2("AlEjAnDRa", "ArAUz")

def function_1(text):
    return text + text

def function_2(text):
    return text.title()

output = function_2(function_1("hello"))
print(output)
