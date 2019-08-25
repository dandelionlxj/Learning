##  题目描述

给定一棵二叉搜索树，请找出其中的第k小的结点。例如， （5，3，7，2，4，6，8）    中，按结点数值大小顺序第三小结点的值为4。



## 思路

二叉搜索树按照中序排序的顺序排序出来的顺序刚好是由小到大的顺序，所以按照中序排序的结果的第k个执就是结果



## 算法

```python
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回对应节点TreeNode
    def __init__(self):
        self.index = 0
    def KthNode(self, pRoot, k):
        # write code here
        if pRoot:
            node = self.KthNode(pRoot.left,k)
            # 当node有值的时候才返回值，避免出现结果值被None覆盖的情况
            if node:
                return node
            self.index +=1
            if self.index == k:
                return pRoot
            node = self.KthNode(pRoot.right,k)
            if node:
                return node
        return None
```

