#!/usr/bin/env python3

'''
Mortgages and loans

This script calculates various mortgages using Canadian formulae.

time -f '%e' ./mortgage_calculator.py > mortgage_calculator.txt
./mortgage_calculator.py > mortgage_calculator.txt
'''


principal = 64300
interest = 3.29
years = 25


payment = principal*(((1+interest/200)**(1/6)-1))/(1-(((1+interest/200)**(1/6)))**-(years*12))
print(payment)

