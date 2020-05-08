# -*- coding: utf-8 -*-
"""
Created on Fri May  8 15:42:22 2020

@author: Desktop
"""
import random

def menu():
    #Ask the player for the numbers
    user_number = get_input_number() 
    #The lottery numbers
    lottery_number = lottery()
    #Print out the winnings
    win_number = user_number.intersection(lottery_number)
    print(f'You matched {len(win_number)} numbers, \n{win_number} \nCongrats! You won £{10**len(win_number)}')
    
#Player choose 6 numbers:
def get_input_number():
    lot_num = input('Enter your 6 digit lottery number, separated by commas:\n>>>').split(',')
    #Set Comprehension
    set_lot = {int(number) for number in lot_num}
    return set_lot

#Lottery calculates randon numbers between 1 and 100.
def lottery():
    values = set()
    while len(values)<6:
        values.add(random.randint(1,100))
    return values

menu()