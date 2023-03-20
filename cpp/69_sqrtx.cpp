#include <iostream>
using namespace std;

class Solution1 {
    // Time: 0 ms; Space: 5.9 MB
public:
    int mySqrt(int x) {
        int left = 1;
        int right = x / 2;
        int middle;
        if (x == 1) return 1;
        while (left <= right) {
            middle = (left + right) / 2;
            if (middle == x / middle && x % middle == 0) {
                return middle;
            } else if (middle <= x / middle) {
                left = middle + 1;
            } else {
                right = middle - 1;
            }
        }
        return left - 1;
    }
};

int main() {
    int val = 17;
    Solution1 solution;
    cout << solution.mySqrt(val) << endl;
}