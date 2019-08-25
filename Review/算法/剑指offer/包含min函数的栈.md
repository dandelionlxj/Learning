##  题目描述

定义栈的数据结构，请在该类型中实现一个能够得到栈中所含最小元素的min函数（时间复杂度应为O（1））  



**解题思路**  

定义两个栈，一个是辅助栈，辅助栈的栈顶一直是最小的数，  

**算法**

```python
# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stack = []
        self.assit = []
    def push(self, node):
        # write code here
        min = self.min()
        if not self.assit or node <= min:
            self.assit.append(node)
        else:
            self.assit.append(min)
        self.stack.append(node)
    def pop(self):
        # write code here
        if self.stack:
            self.assit.pop()
            return self.stack.pop()
    def top(self):
        # write code here
        if self.stack:
            return self.stack[-1]
    def min(self):
        # write code here
        if self.assit:
            return self.assit[-1]
```

