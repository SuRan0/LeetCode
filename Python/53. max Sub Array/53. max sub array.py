# -*-coding:utf-8-*-
def maxSubArray(nums):
    maxSum = nums[0]
    minSum = sum = 0
    for i in range(len(nums)):
        sum += nums[i]
        maxSum = max(maxSum, sum - minSum)
        minSum = min(minSum, sum)

    return maxSum


print(maxSubArray([5,4,-1,7,8]))
