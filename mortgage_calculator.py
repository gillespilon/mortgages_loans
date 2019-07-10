#!/usr/bin/env python3

'''
Mortgages and loans

This script calculates various mortgages using Canadian formulae.

time -f '%e' ./mortgage_calculator.py > mortgage_calculator.txt
./mortgage_calculator.py > mortgage_calculator.txt
'''


import math


principal = 100000
interest = 6
years = 25
pmt = 639.81


payment = (principal*(((1+interest/200)**(1/6)-1)) /
           (1-(((1+interest/200)**(1/6)))**-(years*12)))
print(round(payment, 2))

number_payments = (((math.log(1 - principal *
                   (((1 + interest/200)**(1/6) - 1)) / pmt)) /
                   (-1 * math.log(((1+interest/200)**(1/6))))))
print(round(number_payments, 0))
