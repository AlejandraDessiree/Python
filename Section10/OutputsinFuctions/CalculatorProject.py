
Calc = """
 _____________________
|  _________________  |
| |                 | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|"""

print(Calc)

def calculator(result, num_2):
    pick = str(input("Pick an operation:\nSum = '+'\nMinus = '-'\nDivide = '/'\nMultiplication = '*'\n"))
    num_1 = result
    
    while pick not in ["+", "-", "/", "*"]:
        print("I do not recognize that pick")
        pick = str(input("Pick an operation:\nSum = '+'\nMinus = '-'\nDivide = '/'\nMultiplication = '*'\n"))
        
    if pick == "+":
        result = num_1 + num_2
    elif pick == "-":
        result = num_1 - num_2
    elif pick == "/":
        result = num_1 / num_2
    elif pick == "*":
        result = num_1 * num_2
        
    print(f"{num_1} {pick} {num_2} = {result}")
    
    second_pick = input(f"Type 'y' to continue calculating with {result} or type 'n' to start a new calculation, or type 'stop' to stop the program:\n").lower()
    while second_pick not in ["y", "n", "stop"]:
        print("I do not recognize that pick")
        second_pick = input(f"Type 'y' to continue calculating with {result} or type 'n' to start a new calculation, or type 'stop' to stop the program:\n").lower()
       
    while second_pick in ["y", "n", "stop"]:
        if second_pick == "y":
            num_1 = result
            num_2 = float(input("What's your second number?\n"))
            pick = str(input("Pick an operation:\nSum = '+'\nMinus = '-'\nDivide = '/'\nMultiplication = '*'\n")).lower()
            
            
            while pick not in ["+", "-", "/", "*"]:
                print("I do not recognize that pick")
                pick = str(input("Pick an operation:\nSum = '+'\nMinus = '-'\nDivide = '/'\nMultiplication = '*'\n")).lower()
                
            if pick == "+":
                result = num_1 + num_2
            elif pick == "-":
                result = num_1 - num_2
            elif pick == "/":
                result = num_1 / num_2
            elif pick == "*":
                result = num_1 * num_2
            
                
            print(f"{num_1} {pick} {num_2} = {result}")
            second_pick = input(f"Type 'y' to continue calculating with {result} or type 'n' to start a new calculation, or type 'stop' to stop the program:\n").lower()
            return result
        elif second_pick == "n":
           return calculator(float(input("What's your first number?\n")), float(input("What's your second number?\n")))
        elif second_pick == "stop":
            return " "
    
    
output = calculator(float(input("What's your first number?\n")), float(input("What's your second number?\n")))


print(output)
