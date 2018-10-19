"""
This is a more accurate version of the grinding calculations. It's goal is to compute all possible values.
Currently its in the prototyping stage
"""

import numpy as np
n = 5

a = np.linspace(0,5, num=n)
b = a
c = b+a

"""Platform calculation"""
count_1 = 0
count_2 = 0

while count_1 != n:
    a_el = a.item(count_1)
    b_el = b.item(count_2)
    x = a_el+b_el
    print(x)
    if count_2 !=n:
        count_2 += 1
        b_el = b.item(count_2)
        x = a_el+b_el
        print(x)
    else:
        count_1 =+ 1