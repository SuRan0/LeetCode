# -*-coding:utf-8-*-
"""
Design a stack-like data structure to push elements to the stack
and pop the most frequent element from the stack.

Implement the FreqStack class:

FreqStack() constructs an empty frequency stack.
void push(int val) pushes an integer val onto the top of the stack.
int pop() removes and returns the most frequent element in the stack.
If there is a tie for the most frequent element, the element closest to the stack's top is removed and returned.

Link：https://leetcode.cn/problems/maximum-frequency-stack
"""
import heapq


class FreqStack:

    def __init__(self):
        self.freq = {}  # frequency
        self.time = 0   # time
        self.q = []     # priority queue

    def push(self, val):
        self.freq.setdefault(val, 0)
        self.freq[val] += 1
        self.time += 1
        heapq.heappush(self.q, (-self.freq[val], -self.time, val))  # maximum to first pop

    def pop(self):
        _, _, val = heapq.heappop(self.q)
        self.freq[val] -= 1
        print(val)
        return val

obj = FreqStack()
obj.push(5)
obj.push(7)
obj.push(5)
obj.push(7)
obj.push(4)
obj.push(5)
obj.pop()
obj.pop()
obj.pop()
obj.pop()
