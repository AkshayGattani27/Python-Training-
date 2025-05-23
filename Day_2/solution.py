#Greatest among 2 numbers

def largest_of_two(num1,num2):
    '''This is my first function'''
    if num1 > num2:
        return num1
    else:
        return num2

# Greatest among three numbers

def largest_of_three(num1, num2, num3):
    '''This is my second function'''
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

#Check if vowel or not

def func_vowel(vow):
    '''This is my second function'''
    vowels = ['a','e','i','o','u']
    my_set =set(vowels)  
    if len(vow) == 1 and vow.lower() in my_set:
        return True
    else:
        return False

#Leap Year

year = int(input("Enter the year : "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")
