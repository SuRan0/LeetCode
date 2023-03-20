#include <iostream>
#include <vector>
using namespace std;

class Solution1 {
    // Time: 4 ms; Space: 13.3 MB
public:
    vector<int> myfun1(vector<int>& nums, int target) {
        int leftBorder = getLeftBoarder(nums, target);
        int rightBorder = getRightBoarder(nums, target);
        if (leftBorder == -2 || rightBorder == -2) return {-1, -1};
        if (rightBorder - leftBorder > 1) return {leftBorder + 1, rightBorder - 1};
        return {-1, -1};
    }

private:
    int getRightBoarder(vector<int>& nums, int target) {
        int left = 0;
        int right = nums.size() - 1;
        int rightBorder = -2;
        while (left <= right) {
            int middle = left + ((right - left) / 2);
            if (nums[middle] > target) {
                right = middle - 1;
            } else {    // nums[middle] <= target, update left
                left = middle + 1;
                rightBorder = left;
            }
        }
        return rightBorder;
    }

    int getLeftBoarder(vector<int>& nums, int target) {
        int left = 0;
        int right = nums.size() - 1;
        int leftBorder = -2;
        while (left <= right) {
            int middle = left + ((right - left) / 2);
            if (nums[middle] < target) {
                left = middle + 1;
            } else {    // nums[middle] >= target, update right
                right = middle - 1;
                leftBorder = right;
            }
        }
        return leftBorder;
    }
};

class Solution2 {
    // Time: 8 ms; Space: 13.2 MB
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        return {searchLeftOrRightBound(nums, target, "left"), searchLeftOrRightBound(nums, target, "right")};
    }

private:
    int searchLeftOrRightBound(vector<int>& nums, int target, const string& bound) {
        int left = 0;
        int right = nums.size() - 1;
        int result = -1;
        while (left <= right) {
            int middle = left + ((right - left) / 2);
            if (nums[middle] < target) {
                left = middle + 1;
            } else if (nums[middle] > target) {    // nums[middle] >= target, update right
                right = middle - 1;
            } else {
                result = middle;
                if (bound == "left") {
                    right = middle - 1;
                } else if (bound == "right") {
                    left = middle + 1;
                }
            }
        }
        return result;
    }
};

int main() {
    vector<int> nums {5,7,7,8,8,10};
    int target = 8;
    Solution2 solution;
    cout << solution.searchRange(nums, target)[0] << endl;
    cout << solution.searchRange(nums, target)[1] << endl;
    return 0;
}