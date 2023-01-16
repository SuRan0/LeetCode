# -*-coding:utf-8-*-
def maxSubArray(nums):
    currMaxSum = []
    currMaxSum.append(nums[0])
    maxSum = nums[0]
    for i in range(1, len(nums)):
        currMaxSum.append(max(currMaxSum[i - 1] + nums[i], nums[i]))
        maxSum = max(currMaxSum[i], maxSum)
    return maxSum


print(maxSubArray([5,4,-1,7,8]))