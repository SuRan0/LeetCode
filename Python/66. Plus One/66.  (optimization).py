# -*-coding:utf-8-*-
def plus_one(digits):
    carry = 1
    for i in range(len(digits) - 1, -1, -1):
        digits[i], carry = (carry + digits[i]) % 10, (carry + digits[i]) // 10
    return [carry] + digits if carry else digits

print(plus_one([1, 1, 8]))
