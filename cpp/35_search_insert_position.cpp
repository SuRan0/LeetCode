#include <iostream>
#include <vector>
using namespace std;

int myfun1(vector<int>& nums, int target) {
    // 8 ms, 9.4 MB
    int left = 0;
    int right = nums.size() - 1;
    int middle;
    int last = 0;
    while (left <= right) {
        middle = (left + right) / 2;
        if (nums[middle] > target) {
            right = middle - 1;
            last = 0;
        } else if (nums[middle] < target) {
            left = middle + 1;
            last = 1;
        } else {
            return middle;
        }
    }
    return middle + last;
}

int myfun2(vector<int>& nums, int target) {
    // Time: O(log n), 4 ms; Space: O(1), 9.3 MB
    int left = 0;
    int right = nums.size() - 1;
    int middle;
    while (left <= right) {
        middle = (left + right) / 2;
        if (nums[middle] > target) {
            right = middle - 1;
        } else if (nums[middle] < target) {
            left = middle + 1;
        } else {
            return middle;
        }
    }
    return right + 1;
}

int main() {
    vector<int> nums {1, 3};
    int target = 2;
    cout << myfun1(nums, target) << endl;
    return 0;
}