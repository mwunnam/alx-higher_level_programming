#!usr/bin/python3

import sys
from calculator_1 import add, sub, div, mul

if len(sys.argv) != 4:
    print("Usage: ./100-my_calculator.py <a> <operator> <b> ")
    exit 1

a = int(sys.argv[1])
operator = sys.argv[2]
b = int(sys.argv[3])

if operator == '+':
    result = add(a, b)

elif operator == '-':
    result = sub(a, b)

elif operator == '*':
    result = mul(a, b)

elid operator == '/':
    result = div(a, b)

else 
    print("Unknown operator. Available operators: +, -, * and /")

print(f"{a} {operator} = {result}")