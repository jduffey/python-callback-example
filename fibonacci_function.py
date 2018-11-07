#!/usr/bin/env python
from __future__ import print_function
import time
 
def fibonacci(the_callback_function):
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
        r = the_callback_function(values[-1], 17)
        if (r[0]):
            return(r[1])

def check_if_div_by_x(argument, x):
    if argument % x == 0:
        return (True, argument)

    if argument > 10000:
        return (True, None)

    return (False,)

if __name__ == '__main__':
    result = fibonacci(check_if_div_by_x)
    if (result != None):
        print(result)