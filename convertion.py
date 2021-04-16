# Welcome back to python tutorial, In this
# video we are going to see how to make a convertion program 
# for fahrenheit and celsius

# Inputs
number = float(input("Enter the number: "))
convertion_symbol = input("Enter the convertion symbol: ")

# convertion process
def convert (num,symbol):
    if symbol.upper() == "F":
        result = (num * 9/5) + 32#Formula for fahreheit
        print("{:<8} {:<15}".format("Celsius", "Fahrenheit"))
        print("{:<8} {:<15}".format(num, result))
    elif symbol.upper() == "C":
        result = (num - 32) * 5/9# formula for celsius
        print("{:<8} {:<15}".format("Fahrenheit", "Celsius"))
        print("{:<8} {:<15}".format(num, result))
    elif symbol.lower() == "help":
        print(""" To convert celsius to fahreheit type 'F'
To convert fahreheit tupe 'C'""")
    else :
        print("Enter a valid input")
# the entire code will be in github

# output
convert(number, convertion_symbol)