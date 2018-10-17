"""
This is a more accurate version of the grinding calculations. It's goal is to compute all possible values.
Currently its in the prototyping stage
"""

import numpy as np

a = np.linspace(0,5, num=5)
b = a
c = b+a

"""Platform calculation"""
count_1 = 0
count_2 = 0


while count_1 != 5:
    z = a.item(count_1)
    if count_2 <= 5:
        y = a.item(count_2)
        v = z+y
        print(z, "z")
        count_2 += 1
        print(count_2, "count_2")
    else:
      count_1 += 1
      print(count_1, "count_1")

print(a)
print(b)