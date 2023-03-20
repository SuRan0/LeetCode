#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        int m = matrix.size();
        int n = matrix[0].size();
        vector<int> res(m * n, 0);
        int startx = 0, starty = 0;
        int loop = min(m / 2, n / 2);
        int offset = 1;
        int count = 0;
        int i, j;
        if (m == 1) {
            while (starty < n) {
                res[count++] = matrix[startx][starty++];
            }
            return res;
        }
        if (n == 1) {
            while (startx < m) {
                res[count++] = matrix[startx++][starty];
            }
            return res;
        }
        while (loop--) {
            for (j = starty; j < n - offset; j++) {
                res[count++] = matrix[startx][j];
            }
            for (i = startx; i < m - offset; i++) {
                res[count++] = matrix[i][n - offset];
            }
            for (; j > starty; j--) {
                res[count++] = matrix[m - offset][j];
            }
            for (; i > startx; i--) {
                res[count++] = matrix[i][starty];
            }
            startx++;
            starty++;
            offset++;
        }
        if (count < m * n) {
            if (m <= n) {
                while (starty <= n - offset) {
                    res[count++] = matrix[startx][starty++];
                }
            } else {
                while (startx <= m - offset) {
                    res[count++] = matrix[startx++][starty];
                }
            }
        }
        return res;
    }
};

int main() {
    vector<vector<int>> matrix {{2,3,4},{5,6,7},{8,9,10},{11,12,13}};
    Solution solution;
    solution.spiralOrder(matrix);
}