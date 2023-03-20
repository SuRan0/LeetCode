#include <iostream>
#include <vector>
using namespace std;

class Solution1 {
    // Time: O(n), 20 ms; Space: 18.7 MB
public:
    void moveZeroes(vector<int>& nums) {
        int slowIndex = 0;
        int size = nums.size();
        for (int fastIndex = 0; fastIndex < size; fastIndex++) {
            if (nums[fastIndex] != 0) {
                nums[slowIndex++] = nums[fastIndex];
            }
        }
        while (slowIndex < size) {
            nums[slowIndex++] = 0;
        }
    }
};

class Solution2 {
    // Time: O(n), 20 ms; Space: 18.7 MB
public:
    void moveZeroes(vector<int>& nums) {
        int size = nums.size();
        int left = 0;
        int right = 0;
        while (right < size) {
            if (nums[right]) {
                swap(nums[left], nums[right]);
                left++;
            }
            right++;
        }
    }
};

int main() {
    vector<int> nums {1,0,3,12};
    Solution2 solution;
    solution.moveZeroes(nums);
}