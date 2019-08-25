##  题目描述

小明很喜欢数学,有一天他在做数学作业时,要求计算出9~16的和,他马上就写出了正确答案是100。但是他并不满足于此,他在想究竟有多少种连续的正数序列的和为100(至少包括两个数)。没多久,他就得到另一组连续正数和为100的序列:18,19,20,21,22。现在把问题交给你,你能不能也很快的找出所有和为S的连续正数序列? Good Luck!  



**思路**  

想到一个类似滑动窗口的机制，窗口最左边为left，最右边为right，当这窗口里的值大于S时，窗口需要缩小，就将left往右移，如果窗口里的值小于S的话，就将right往右移，找到一个满足条件的序列则添加到结果中，然后左右都往右移，继续寻找下一个序列，直到left到达（S+1）/2处，就不用继续了，因为下面两个数相加肯定大于S

```python
# -*- coding:utf-8 -*-
class Solution:
    def FindContinuousSequence(self, tsum):
        # write code here
        left,right,total=1,2,3
        result=[]
        while left<(tsum+1)/2:
            if total > tsum:
                total-=left
                left+=1
            else:
                if total == tsum:
                    result.append([i for i in range(left,right+1)])
                right+=1
                total+=right
        return result
```



