# -*-coding:utf-8-*-
"""
You are given an integer array nums and an integer k.
You can partition the array into at most k non-empty adjacent subarrays.
The score of a partition is the sum of the averages of each subarray.

Note that the partition must use every integer in nums,
and that the score is not necessarily an integer.

Return the maximum score you can achieve of all the possible partitions.
Answers within 10-6 of the actual answer will be accepted.

"""
nums = [4,1,7,5,6,2,3]
k = 4

score = 0
nums = sorted(nums, reverse=True)
for i in range(k-1):
    score += nums[i]

rest = 0
for i in range(k-1, len(nums)):
    rest += nums[i]
score += rest/(len(nums) - k+1)
print(score)

# wrong: not adjacent subarrays

