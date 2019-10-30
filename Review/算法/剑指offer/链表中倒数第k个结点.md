输入一个链表，输出该链表中倒数第k个结点。  

**解题思路**  
求倒数第k个结点，就用一把长度为k的尺子，当这把尺子的最右端到达链尾时，这把尺子的最左端就是k结点的位置  
 设置两个指针，p1，p2，先让p2走k-1步，然后再一起走，直到p2为最后一个 时，p1即为倒数第k个节点  

 **算法**  
 ```python
# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        if head == None or k <= 0 :
            return None
        p = head
        q = head
        i=0
        while p:
            if i>=k:
                q=q.next
            p=p.next
            i+=1
        return q if i>=k else None
 ```

