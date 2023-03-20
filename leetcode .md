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
// O(log n)
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



##二分法
[704. 二分查找](https://leetcode.cn/problems/binary-search/)

题目：给定一个 n 个元素有序的（升序）整型数组 nums 和一个目标值 target  ，写一个函数搜索 nums 中的 target，如果目标值存在返回下标，否则返回 -1。

```
输入: nums = [-1,0,3,5,9,12], target = 9
输出: 4
解释: 9 出现在 nums 中并且下标为 4
```
二分法找到的right是target的左边一个。index = right + 1

[35. 搜索插入位置](https://leetcode.cn/problems/search-insert-position/)

[34. 在排序数组中查找元素的第一个和最后一个位置](https://leetcode.cn/problems/find-first-and-last-position-of-element-in-sorted-array/)

[69. x的平方根](https://leetcode.cn/problems/sqrtx/)

[367. 有效的完全平方数](https://leetcode.cn/problems/valid-perfect-square/)

##双指针
[27. 移除元素](https://leetcode.cn/problems/remove-element/)

[26. 删除有序数组中的重复项](https://leetcode.cn/problems/remove-duplicates-from-sorted-array/)

[283. 移动零](https://leetcode.cn/problems/move-zeroes/)

[844. 比较含退格的字符串](https://leetcode.cn/problems/backspace-string-compare/)

[977. 有序数组的平方](https://leetcode.cn/problems/squares-of-a-sorted-array/)  
双指针，左右往中间走

##滑动窗口
[209. 长度最小的子数组](https://leetcode.cn/problems/minimum-size-subarray-sum/)  
滑动窗口

[904. 水果成篮](https://leetcode.cn/problems/fruit-into-baskets/)

[76. 最小覆盖子串](https://leetcode.cn/problems/minimum-window-substring/)

##模拟行为
[59. 螺旋矩阵II](https://leetcode.cn/problems/spiral-matrix-ii/)

[54. 螺旋矩阵](https://leetcode.cn/problems/spiral-matrix/)

#链表
##链表理论基础
+ 单链表
+ 双链表
+ 循环链表

###链表的存储方式
+ 内存不是连续分布
+ 链表通过指针与的指针链在内存中的各个节点

##虚拟头节点
[203. 移除链表元素](https://leetcode.cn/problems/remove-linked-list-elements/)

##链表基本操作
[707. 设计链表](https://leetcode.cn/problems/design-linked-list/)

##反转链表
[206. 反转链表](https://leetcode.cn/problems/reverse-linked-list/)  
pre和cur两个，建立一个tmp

##两两交换链表中的节点
[24. 两两交换链表中的节点](https://leetcode.cn/problems/swap-nodes-in-pairs/)

##删除链表的倒数第N个节点
[19. 删除链表的倒数第N个节点](https://leetcode.cn/problems/remove-nth-node-from-end-of-list/)
快慢指针，fast 先走 n+1 步

##相交链表
[160. 相交链表](https://leetcode.cn/problems/intersection-of-two-linked-lists/)
遍历得出A和B的length，把listA设为最长，移动到与listB对其的位置，判断是否一致，curA == curB, return curA

##环形链表II
[142. 环形链表II](https://leetcode.cn/problems/linked-list-cycle-ii/)
先让fast走两步，slow走一步，找到相遇节点，然后让fast从相遇节点出发，每次走一步，slow从head出发，每次走一步，再次相遇在入口节点

#哈希表
##哈希表理论基础
+ 一般使用哈希表快速判断一个元素是否出现在集合里。
+ 哈希表是根据关键码的值而直接进行访问的数据结构。

###哈希函数
+ hashFunction = hashCode(name) % tableSize;
+ index = hashFunction(name)
+ 通过hashCode把名字转换成数值

###哈希碰撞
+ 两个名字同时映射到哈希表，同一个索引下标的位置。

####拉链法
+ 发生冲突的元素都被存储在链表中

####线性探测法
+ tableSize > dataSize, 找下一个空位置放置冲突信息

##常见的哈希结构
+ 数组
+ 集合 set
+ 映射 map

+ unodered_set/map：哈希表
+ set/map, multiset/map：红黑树，key是有序的，不可修改，只能删除和增加，平衡二叉搜索树

+ 使用集合：优先使用unorder_set >(有序)> set >(有重复数据)> multiset

##有效的字母异位词
[242. 有效的字母异位词](https://leetcode.cn/problems/valid-anagram/) 
s[i] - 'a'作为一个值，记录在record相对应的索引值里。

[383. 赎金信](https://leetcode.cn/problems/ransom-note/)
如果用map，空间消耗更大

[49. 字母异位词分组](https://leetcode.cn/problems/group-anagrams/)


#1
##2
###3
a<sub>n</sub>