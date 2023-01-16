# -*-coding:utf-8-*-
def plusOne(digits):
    if digits[-1] != 9:
        last = digits[-1] + 1
        digits.pop()
        digits.append(last)
    else:
        digits.pop()
        i = 1
        while(i != 0):
            if digits and digits[-1] == 9:
                digits.pop()
                i = i + 1
            elif digits:
                last2 = digits[-1] + 1
                digits.pop()
                digits.append(last2)
                for x in range(i):
                    digits.append(0)
                i = 0
            if not digits:
                digits = [1]
                for x in range(i):
                    digits.append(0)
                i = 0
    return digits


print(plusOne([9,9]))
