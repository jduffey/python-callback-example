#!/usr/bin/env python
from __future__ import print_function
import time
 
def fibonacci(first_callback_function, second_callback_function):
    values = []
    while(True):
        if len(values) < 2:
            values.append(1)
        else:
            values = [values[-1], values[-1] + values[-2]]
        print(values)
        time.sleep(.25)

        '''
        This is where we allow the primary function to run its
        callback (secondary??) function
        in such a way that the primary and "secondary" functions
        can have their code separate.
        '''
        first_result = first_callback_function(values[-1], 17)
        if (first_result[0]):
            return(first_result[1])

        second_result = second_callback_function(values[-1])
        print(second_result)

def check_if_div_by_x(argument, x):
    if argument % x == 0:
        return (True, argument)

    if argument > 10000:
        return (True, None)

    return (False,)

def double_the_number(argument):
    return argument * 2

if __name__ == '__main__':
    result = fibonacci(check_if_div_by_x, double_the_number)
    if (result != None):
        print(result)