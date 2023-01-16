# -*-coding:utf-8-*-
"""
数学 + 二分查找。
令 f(x) 等于所有小于等于 x 的神奇数字的数量，f(x) 是单调递增的。
所以我们可以使用二分查找找到第一个使 f(x) = n 的 x 的值。x 即为答案。

如何求 f(x) ？在区间 [0, x] 中有 x/a 个数能被 a 整除，有 x/b 个数能被 b 整除。
但是 f(x) 不等于 x/a + x/b。因为区间 [0, x] 中有一些数既能被 a 整除也能被 b 整除，它们被加了两次，所以要减去这些数。

令 lcm 为 a 和 b 的最小公倍数。区间 [0, x] 既能被 a 整除也能被 b 整除的数就是 lcm 的倍数，它们有 x/lcm 个。

所以 f(x) = x/a + x/b - x/lcm。

其中，lcm 可以根据 a 和 b 的最大公约数（gcd）求出：lcm(a, b) = a * b / gcd(a, b)。gcd 可以用辗转相除法求出。
"""

n, a, b = 3, 6, 4

def gcd(a, b):   # greatest common divisor
    if a > b:
        a, b = b, a
    if b%a == 0:
        return a
    else:
        return gcd(b%a, a)

MOD = 1e9 + 7
lcm = a * b / gcd(a, b)    # least common multiple
r = max(a, b) * n
l = min(a, b)
while l < r:
    mid = (l + r) >> 1   # (l+r)/2, math.floor
    cnt = mid//a + mid//b -mid//lcm
    if cnt >= n:
        r = mid
    else:
        l = mid + 1
print(int(l % MOD))
