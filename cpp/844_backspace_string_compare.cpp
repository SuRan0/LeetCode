#include <iostream>
using namespace std;

class Solution {
public:
    bool backspaceCompare(string s, string t) {
        return backspaceString(s) == backspaceString(t);
    }

private:
    string backspaceString(string s) {
        int left = 0;
        for (int right = 0; right < s.size(); right++) {
            if (s[right] != '#') {
                s[left++] = s[right];
            } else {
                left--;
            }
        }
        return s.substr(0, left);
    }
};

int main() {
    string s = "ab#c";
    string t = "ad#c";
    Solution solution;
    solution.backspaceCompare(s, t);
}