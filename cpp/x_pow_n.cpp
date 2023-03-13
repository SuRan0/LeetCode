#include <iostream>
#include <vector>
using namespace std;

int function3(int x, int n) {
    if (n == 0) {
        return 1;
    }
    if (n % 2 == 1) {
        return function3(x, n / 2) * function3(x, n / 2)*x;
    }
    return function3(x, n / 2) * function3(x, n / 2);
}

int function4(int x, int n) {
    if (n == 0) {
        return 1;
    }
    int t = function4(x, n / 2);    // 相对于function3, 把递归操作抽取出来
    if (n % 2 == 1) {
        return t * t * x;
    }
    return t * t;
}

int main() {
    cout << function3(2, 3) << endl;
    return 0;
}