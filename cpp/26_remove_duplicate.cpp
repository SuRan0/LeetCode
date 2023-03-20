#include <iostream>
#include <vector>
using namespace std;

class Solution {
    // Time: O(n), 8 ms; Space: O(1), 17.8 MB
public:
    int removeDuplicates(vector<int>& nums) {
        int slowIndex = 1;
        for (int fastIndex = 1; fastIndex < nums.size(); fastIndex++) {
            if (nums[fastIndex] != nums[fastIndex - 1]) {
                nums[slowIndex++] = nums[fastIndex];
            } 
        }
        return slowIndex;
    }
};

int main() {
    vector<int> nums {0,0,1,1,1,2,2,3,3,4};
    Solution solution;
    cout << solution.removeDuplicates(nums) << endl;
}