#!/usr/bin/env python
from __future__ import print_function
import time
 
def fibonacci(callbackFunction):
    values = []
    while(True):
        if len(values) < 2:
            values.append(1)
        else:
            values = [values[-1], values[-1] + values[-2]]
        print(values)
        time.sleep(.25)

        r = callbackFunction(values[-1])
        if (r[0]):
            return(r[1])

def check_17(valueToAssess):
    if valueToAssess % 17 == 0:
        return (True, valueToAssess)

    if valueToAssess > 10000:
        return (True, None)

    return (False,)

if __name__ == '__main__':
    result = fibonacci(check_17)
    if (result != None):
        print(result)