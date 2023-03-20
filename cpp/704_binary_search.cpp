#include <iostream>
#include <vector>
using namespace std;

int myfun1(vector<int>& nums, int target) {
    // Time: O(n), 24ms; Space: O(1), 26.9 MB
    int idx = -1;
    for (unsigned int i = 0; i < nums.size(); i++) {
        if (nums[i] == target) {
            idx = i;
        }
    }
    return idx;
}

int method1(vector<int>& nums, int target) {
    // Time: O(log n), 32 ms; Space: O(1), 26.9 MB
    int left = 0;
    int right = nums.size() - 1;
    while (left <= right) {
        int middle = left + ((right - left) / 2);   // 防止溢出
        if (nums[middle] > target) {
            right = middle - 1;     // target in left range
        } else if (nums[middle] < target) {
            left = middle + 1;
        } else {
            return middle;
        }
    }
    return -1;
}

int method2(vector<int>& nums, int target) {
    // Time: O(log n), 24 ms; Space: O(1), 26.9 MB
    int left = 0;
    int right = nums.size();
    while (left < right) {
        int middle = left + ((right - left) / 2);   // 防止溢出
        if (nums[middle] > target) {
            right = middle;     // target in left range
        } else if (nums[middle] < target) {
            left = middle + 1;
        } else {
            return middle;
        }
    }
    return -1;
}

int main() {
    vector<int> nums {-1, 0, 3, 5, 9, 12};
    int target = 9;
    cout << method2(nums, target) << endl;
    return 0;
}