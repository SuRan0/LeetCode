# -*-coding:utf-8-*-
"""
You are given an integer array nums (0-indexed). In one operation, you can choose an element of the array and increment it by 1.

For example, if nums = [1,2,3], you can choose to increment nums[1] to make nums = [1,3,3].
Return the minimum number of operations needed to make nums strictly increasing.

An array nums is strictly increasing if nums[i] < nums[i+1] for all 0 <= i < nums.length - 1. An array of length 1 is trivially strictly increasing.

Link：https://leetcode.cn/problems/minimum-operations-to-make-the-array-increasing
Time: 2022.12.11
"""
nums = [4,2,6,2,2,3,5,7,10,6,4,1,3,9,10,6,5,5,7,7,9,8,2,4,7,4,10,1,10,4,4,4,7,7,4,10,3,5,6,1,5,8,8,3,3,1,6,7,9,6,9,8,6,10,2,10,5,9,5,7,1,5,2,8,2,9,4,10,5,7,6,4,1,2,10,9,9,9,3,3,5,1,2,4,1,1,7,1,2,1,1,1,9,6,6,1,10,1,9,4,8,4,5,5,10,9,9,5,4,3,4,7,1,4,9,8,1,6,6,7,2,1,10,3,9,2,3,4,4,3,5,2,1,6,3,2,8,3,4,1,5,6,1,10,2,8,4,4,3,2,1,4,1,2,2,4,5,5,9,7,4,1,5,4,6,6,6,8,10,7,7,2,7,4,8,6,3,10,2,4,2,7,5,9,5,6,6,7,8,6,6,6,7,8,9,1,6,3,5,3,5,10,3,9,3,3,8,3,3,3,2,10,5,4,6,6,3,5,8,5,2,7,3,9,6,8,2,3,6,2,3,8,9,1,1,4,6,6,9,6,9,6,6,2,3,7,1,5,10,4,1,4,5,6,10,7,4,6,1,4,5,10,1,4,2,3,4,6,9,5,3,3,4,2,5,10,9,9,9,10,9,7,8,10,9,8,3,9,6,4,7,2,5,4,4,3,3,4,1,3,8,6,3,1,6,2,10,4,4,2,8,4,10,6,3,10,1,4,6,8,9,1,1,6,8,9,6,3,8,2,9,6,10,5,10,6,10,2,8,6,7,2,5,2,6,1,3,6,4,6,5,5,5,8,7,1,5,3,5,1,2,7,7,10,4,5,6,10,8,10,5,10,5,3,6,3,6,2,7,6,9,10,4,7,8,3,8,4,1,4,2,2,1,9,9,8,10,8,6,9,3,10,8,7,1,7,9,9]


count = 0
nums2 = {}
seperate = 0
while len(nums) != 1 and len(nums) != 0:
    max_num = max(nums)
    max_i = nums.index(max_num)
    for i in range(1, len(nums) - max_i):
        operators = max_num + i - nums[max_i+i]
        nums[max_i + i] += operators
        count += operators
    if nums2:
        if nums[-1] >= nums2[seperate-1][0]:
            operators = nums[-1] - nums2[seperate-1][0] + 1
            count += operators * len(nums2[seperate-1])
            for i in range(len(nums2[seperate-1])):
                nums2[seperate-1][i] += operators
        for j in range(seperate-1, 0, -1):
            if nums2[j][-1] >= nums2[j-1][0]:
                operators = nums2[j][-1] - nums2[j-1][0] + 1
                count += operators * len(nums2[j-1])
                for i in range(len(nums2[j-1])):
                    nums2[j-1][i] += operators
    nums2[seperate] = nums[max_i: ]
    nums = nums[0: max_i]
    seperate += 1

print(count)
print(nums2)
