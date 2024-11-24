def is_leap_year(year):
    """ If the value that returns is:
    True: Is a leap year
    False : Its not a leap year
    """
    leap = True
    value = 0
    
    if year % 4 == 0:
        leap = True
        if year % 100 == 0:
            leap = False
            if year % 400 == 0:
                leap = True
            elif year % 400 != 0:
                leap = False
        elif year % 100 == 0:
            leap = False
    elif year % 4 != 0:
        leap = False
        
    return leap

result = is_leap_year(int(input("What year you want to check?\n")))

print(result)


# This is
# a comment
# to try ctr + /
