#!/usr/bin/env python3

'''
Mortgages and loans

This script calculates various mortgages using Canadian formulae.

time -f '%e' ./mortgage_calculator.py > mortgage_calculator.txt
./mortgage_calculator.py > mortgage_calculator.txt

                               i    1/comp
                       ( 1 +  --- )       -   1
                              200
Payment = Principal x  ------------------------
                                    i   1/comp -12 x n
                       1 -  [ (1 + --- )     ]
                                   200
'''


import math


def monthly_payment(principal, interest, years, compounding, payment_plus):
    '''
    Calculate the monthly payment with twice-a-year compounding.
    '''
    payment_monthly = (principal*(((1+interest/200)**(1/compounding)-1)) /
                       (1-(((1+interest/200)**(1/compounding)))**-(years*12)))
    accrued_interest = payment_monthly * 12 * years - principal
    print(f'\nPrincipal:               {principal:<10,.2f} CAD'
          .replace(',', ' '),
          f'\n'
          f'Interest:                {interest:10.2f} %\n'
          f'Amortization:            {years:7.0f}    years\n'
          f'Monthly payment to make: {payment_monthly:10.2f} CAD\n'
          f'Accrued interest:        {accrued_interest:10.2f} CAD\n')


def number_payments(principal, interest, compounding, payment_plus):
    '''
    Calculate the number of monthly payments for an input amount with
    twice-a-year compounding.
    '''
    number_payments = (((math.log(1 - principal *
                       (((1 + interest/200)**(1/compounding) - 1)) /
                       payment_plus)) /
                       (-1 * math.log(((1+interest/200)**(1/compounding))))))
    accrued_interest_two = payment_plus * number_payments - principal
    print(f'\nPrincipal:               {principal:<10,.2f} CAD'
          .replace(',', ' '),
          f'\n'
          f'Interest:                {interest:10.2f} %\n'
          f'Monthly payment made:    {payment_plus:10.2f} CAD\n'
          f'Number of payments:      {number_payments:7.0f}\n'
          f'Accrued interest:        {accrued_interest_two:10.2f} CAD\n')


def getinfo():
    '''
    Ask the user for inputs for the mortgage calculations.
    '''
    principal = float(input('What is the principal amount?           '))
    interest = float(input('What is the interest rate (%)?          '))
    years = float(input('What is the amortization period (year)? '))
    compounding = float(input('Months of compounding?                  '))
    payment_plus = float(input('What monthly payment would you make?    '))
    return principal, interest, years, compounding, payment_plus


if __name__ == '__main__':
    principal, interest, years, compounding, payment_plus = getinfo()
    monthly_payment(principal, interest, years, compounding, payment_plus)
    number_payments(principal, interest, compounding, payment_plus)
