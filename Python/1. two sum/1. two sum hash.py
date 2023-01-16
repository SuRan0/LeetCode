nums = [3, 2, 3, 5]
target = 8
hashtable = dict()
for i, num in enumerate(nums):
    if target - num in hashtable:
        print([hashtable[target - num], i])
    hashtable[nums[i]] = i