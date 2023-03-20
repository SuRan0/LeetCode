#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;

class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> mp;
        for (string& str: strs) {
            string key = str;
            sort(key.begin(), key.end());
            mp[key].emplace_back(str);
        }
        vector<vector<string>> ans;
        for (auto it = mp.begin(); it != mp.end(); it++) {
            ans.emplace_back(it->second);
        }
        return ans;
    }
};

int main() {
    vector<string> strs {"eat", "tea", "tan", "ate", "nat", "bat"};
    Solution solution;
    solution.groupAnagrams(strs);
}
