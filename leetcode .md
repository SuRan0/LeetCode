#Leetcode刷题
##算法性能分析
###时间复杂度
+ 时间复杂度用来定性描述算法的运行时间。
+ 大O用来表示上界。

O(1) < O(logn) < O(n) < O(n^2) < O(n^3) < O(2^n)

### 递归算法的时间复杂度
面试题：求x的n次方

``` cpp
// O(n)
int function1(int x, int n) {
	int result = 1;
	for (int i = 0; i < n; i++) {
		result = result * x;
	}
	return result;
}
```

**递归算法**  
时间复杂度：递归次数*每次递归中的操作次数
递归n次O(n)，每次进行一个乘法操作O(1) -> n x 1 = O(n)

``` cpp
// O(n)
int function2(int x, int n) {
	if (n == 0) {
		return 1;
	}
	return function2(x, n-1) * x;
}
```

``` cpp
// O(n)
int function3(int x, int n) {
	if (n == 0) {
		return 1;
	}
	if (n % 2 == 1) {
		return function3(x, n / 2) * function3(x, n / 2)*x;
	} 
	return function3(x, n / 2) * function3(x, n / 2);
}
```
e.g. x=2, n=3, solution=8，因为fun(x, 0)为1，fun(x, 1)为x

| fun |  return  | back |
|---|---|---|
|fun(2, 3)| fun(2, 1) * fun(2, 1) *  2 | 8 |
| fun(2, 1) | fun(2, 0) * fun(2, 0) * 2 | 2 |
| fun(2, 0) | 1 | 1 |

![二叉树](https://code-thinking-1253855093.file.myqcloud.com/pics/20201209193909426.png)

每个节点代表一次递归并进行一次乘法。递归次数 -> 节点数量

n = 16, 节点数=2<sup>m+1</sup>-1=n-1，m为深度，m=log<sub>2</sub>n-1

``` cpp
// O(logn)
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
```

###空间复杂度
+ 空间复杂度是考虑程序运行时占用的内存大小。


#数组
##数组理论基础
+ 数据是存放在连续内存空间上的相同类型数据的结合。
+ C++中，vector的底层实现是array。
+ 数组的元素是不能删的，只能覆盖。



##二分查找
[704. 二分查找](https://leetcode.cn/problems/binary-search/)

题目：给定一个 n 个元素有序的（升序）整型数组 nums 和一个目标值 target  ，写一个函数搜索 nums 中的 target，如果目标值存在返回下标，否则返回 -1。


#1
##2
###3
a<sub>n</sub>