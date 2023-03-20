def myfun1(nums, target):
    # Time: O(n), 44 ms; Space: O(1), 16.1 MB
    idx = -1
    for i in range(0, len(nums)):
        if nums[i] == target:
            idx = i
    return idx

def method1(nums, target):
    # Time: O(log n), 36 ms; Space: O(1), 16.1 MB
    left = 0
    right = len(nums) -1
    while left <= right:
        middle = int((left + right) / 2)
        if nums[middle] > target:
            right = middle - 1
        elif nums[middle] < target:
            left = middle + 1
        else:
            return middle
    return -1

def method2(nums, target):
    # Time: O(log n), 44 ms; Space: O(1), 16 MB
    left, right = 0, len(nums)
    while left < right:
        middle = left + (right - left) // 2
        
        if nums[middle] > target:
            right = middle
        elif nums[middle] < target:
            left = middle + 1
        else:
            return middle
    return -1

def main():
    nums = [-1, 0, 3, 5, 9, 12]
    target = 9
    print(method1(nums, target))

if __name__ == "__main__":
    main()
