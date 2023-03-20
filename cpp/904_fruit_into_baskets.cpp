#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int totalFruit(vector<int>& fruits) {
        vector<int> basket(2);
        int result = 0;
        int i = 0;
        int subLength = 0;
        for (int j = 0; j < fruits.size(); j++) {
            if (j == 0) {
                basket[0] = fruits[j];
                basket[1] = fruits[j];
            }
            if (basket[0] == basket[1] && fruits[j] != basket[1]) {
                basket[1] = fruits[j];
            }
            if (fruits[j] != basket[0] && fruits[j] != basket[1]) {
                basket[0] = basket[j - 1];
                basket[1] = fruits[j];
                i = j - 1;
                while (fruits[i - 1] == basket[0]) {
                    i--;
                }
            } else {
                subLength = j - i + 1;
                result = result < subLength ? subLength : result;
            }
        }
        return result;
    }
};

int main() {
    vector<int> fruits {3,3,3,1,2,1,1,2,3,3,4};
    Solution solution;
    solution.totalFruit(fruits);
}