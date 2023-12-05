import numpy as np
 
def multi_func(massive):
    mult = 1
    for element in massive:
        mult = mult * element

    print(mult)

a = [1,2,3,4,5,6,7,8,9]
list=np.array(a)

multi_func(list)