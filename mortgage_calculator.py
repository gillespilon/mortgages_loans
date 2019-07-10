#!/usr/bin/env python3

'''
Mortgages and loans

This script calculates various mortgages using Canadian formulae.

time -f '%e' ./mortgage_calculator.py > mortgage_calculator.txt
./mortgage_calculator.py > mortgage_calculator.txt
'''


import math


principal = float(input('What is the principal amount?           '))
interest = float(input('What is the interest rate (%)?          '))
years = float(input('What is the amortization period (year)? '))
years = 25
pmt = 639.81


payment = (principal*(((1+interest/200)**(1/6)-1)) /
           (1-(((1+interest/200)**(1/6)))**-(years*12)))
print(f'Principal:               {principal} CAD\n'
      f'Interest:                {interest} %\n'
      f'Amortization:            {years} years\n'
      f'Monthly payment to make: {round(payment, 2)} CAD\n')


number_payments = (((math.log(1 - principal *
                   (((1 + interest/200)**(1/6) - 1)) / pmt)) /
                   (-1 * math.log(((1+interest/200)**(1/6))))))
print(f'Principal:               {principal} CAD\n'
      f'Interest:                {interest} %\n'
      f'Monthly payment made:    {pmt} CAD\n'
      f'Number of payments:      {round(number_payments, 0)}')
