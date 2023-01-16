# -*-coding:utf-8-*-
"""
You are given an integer array nums and an integer k.
You can partition the array into at most k non-empty adjacent sub-arrays.
The score of a partition is the sum of the averages of each subarray.

Note that the partition must use every integer in nums,
and that the score is not necessarily an integer.

Return the maximum score you can achieve of all the possible partitions.
Answers within 10-6 of the actual answer will be accepted.

"""
nums = [9,1,2,3,9]
k = 3

n = len(nums)
# pre-processing
total = [0] * (n+1)
for i in range(1, n+1):
    total[i] = total[i-1] + nums[i-1]

# dp[i-1][k-1]: largest sum of averages of the first i elements from 'nums'  into k sub-arrays
dp=[[0]*k for _ in range(n)]
# base case: k=1
for i in range(n):
    dp[i][0] = total[i+1]/(i+1)
for i in range(n):
    for j in range(1, k):
        for x in range(i):
            avg = (total[i+1] - total[x+1])/(i-x)
            dp[i][j] = max(dp[i][j], dp[x][j-1] + avg)
print(dp[n-1][k-1])
