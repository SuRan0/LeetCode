# -*-coding:utf-8-*-
# 不能直接len(list(set(nums)))，因为改变内存地址了
def removeDuplicates(nums):
    new = sorted(list(set(nums))) # set()会把负数弄到list后面
    for i in range(len(new)):
        nums[i] = new[i]
    return new


print(removeDuplicates([-1,0,0,0,0,3,3]))
