#!/usr/bin/env python3

'''
Mortgages and loans

This script calculates various mortgages using Canadian formulae.

time -f '%e' ./mortgage_calculator.py > mortgage_calculator.txt
./mortgage_calculator.py > mortgage_calculator.txt

                               i    1/6
                       ( 1 +  --- )       -   1
                              200
Payment = Principal x  ------------------------
                                    i   1/6    -12 x n
                       1 -  [ (1 + --- )     ]
                                   200
'''


import math


def monthly_payment(principal, interest, years, pmt):
    payment = (principal*(((1+interest/200)**(1/6)-1)) /
               (1-(((1+interest/200)**(1/6)))**-(years*12)))
    accrued_interest = payment * 12 * years - principal
    print(f'\nPrincipal:               {principal:<10,.2f} CAD'
          .replace(',', ' '),
          f'\n'
          f'Interest:                {interest:10.2f} %\n'
          f'Amortization:            {years:7.0f}    years\n'
          f'Monthly payment to make: {payment:10.2f} CAD\n'
          f'Accrued interest:        {accrued_interest:10.2f} CAD\n')


def monthly_payment(principal, interest, pmt):
    number_payments = (((math.log(1 - principal *
                       (((1 + interest/200)**(1/6) - 1)) / pmt)) /
                       (-1 * math.log(((1+interest/200)**(1/6))))))
    accrued_interest_two = pmt * number_payments - principal
    print(f'\nPrincipal:               {principal:<10,.2f} CAD'
          .replace(',', ' '),
          f'\n'
          f'Interest:                {interest:10.2f} %\n'
          f'Monthly payment made:    {pmt:10.2f} CAD\n'
          f'Number of payments:      {number_payments:7.0f}\n'
          f'Accrued interest:        {accrued_interest_two:10.2f} CAD\n')


def getinfo():
    principal = float(input('What is the principal amount?           '))
    interest = float(input('What is the interest rate (%)?          '))
    years = float(input('What is the amortization period (year)? '))
    pmt = float(input('What monthly payment would you make?    '))
    return principal, interest, years, pmt


if __name__ == '__main__':
    principal, interest, years, pmt = getinfo()
    monthly_payment(principal, interest, years, pmt)
    monthly_payment(principal, interest, pmt)
