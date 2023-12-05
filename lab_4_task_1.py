import numpy as np


def avg(n):
    m = np.average(n)

    print(m)


a = [1,2,3,4,6,7,8]
list = np.array(a)
avg(list)