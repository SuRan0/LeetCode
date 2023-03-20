#include <iostream>
#include <vector>
using namespace std;

class Solution1 {
    // 暴力求解
    // Time: O(n^2), 4 ms; Space: O(1), 8.5 MB
public:
    int removeElement(vector<int>& nums, int val) {
        int size = nums.size();
        for (int i = 0; i < size; i++) {
            if (nums[i] == val) {
                for (int j = i + 1; j < size; j++) {
                    nums[j - 1] = nums[j];
                }
                i--;    // remove 1 element, i move forward
                size--;
            }
        }
        return size;
    }
};

class Solution2 {
    // double pointer method
    // Time: O(n), 0 ms; Space: O(1), 8.5 MB
public:
    int removeElement(vector<int>& nums, int val) {
        int slowIndex = 0;
        for (int fastIndex = 0; fastIndex < nums.size(); fastIndex++) {
            if (val != nums[fastIndex]) {
                nums[slowIndex++] = nums[fastIndex];
            }
        }
        return slowIndex;
    }
};

class Solution3 {
    // similar double pointer method, ensure to move minimum number of elements
    // 检测出第一个是val的元素，把最后一个不是val的元素替换过去，再继续检测
    // Time: O(n), 0 ms; Space: O(1), 8.7 MB
public:
    int removeElement(vector<int>& nums, int val) {
        int leftIndex = 0;
        int rightIndex = nums.size() - 1;
        while (leftIndex <= rightIndex) {
            // find the left elements that equals to "val"
            while (leftIndex <= rightIndex && nums[leftIndex] != val) {
                leftIndex++;
            }
            // find the right element that != val
            while (leftIndex <= rightIndex && nums[rightIndex] == val) {
                rightIndex--;
            }
            // cover the right-not-equal element to left-equal element
            if (leftIndex < rightIndex) {
                nums[leftIndex++] = nums[rightIndex--];
            }
        }
        return leftIndex;
    }
};

int main() {
    vector<int> nums {0,1,2,2,3,0,4,2};
    int val = 2;
    Solution3 solution;
    cout << solution.removeElement(nums, val) << endl;
}