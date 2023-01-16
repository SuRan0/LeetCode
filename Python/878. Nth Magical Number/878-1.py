# -*-coding:utf-8-*-
"""
A positive integer is magical if it is divisible by either a or b.

Given the three integers n, a, and b, return the nth magical number.
Since the answer may be very large, return it modulo 109 + 7.
"""

n, a, b = 4, 2, 3

i = 0
for j in range(1, int(1e9)):
    if j%a == 0:
        i += 1
    elif j%b == 0:
        i += 1
    if i == n:
        print(j)
        break

# time expand