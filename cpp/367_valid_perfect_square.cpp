#include <iostream>
using namespace std;

class Solution {
    // Time: 0 ms; Space: 5.9 MB
public:
    bool isPerfectSquare(int num) {
        int left = 1;
        int right = num / 2;
        int middle;
        if (num == 1) return true;
        while (left <= right) {
            middle = (left + right) / 2;
            if (middle == num / middle && num % middle == 0) {
                return true;
            } else if (middle <= num / middle) {
                left = middle + 1;
            } else {
                right = middle - 1;
            }
        }
        return false;
    }
};

int main() {
    int num = 1;
    Solution solution;
    cout << solution.isPerfectSquare(num) << endl;
}