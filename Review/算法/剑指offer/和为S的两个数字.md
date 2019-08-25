##  题目描述

输入一个递增排序的数组和一个数字S，在数组中查找两个数，使得他们的和正好是S，如果有多对数字的和等于S，输出两个数的乘积最小的。

## 输出描述:

```
对应每个测试案例，输出两个数，小的先输出。
```

 

**思路**  

此处可能会被题目误导，输出两个数的乘积最小，而距离越远的乘积越小，如如7+8=15 1+14=15乘积1*14小，所以从头和尾开始匹配，找到符合条件的两个数就是乘积最小的两个数



**算法**

```python
# -*- coding:utf-8 -*-
class Solution:
    def FindNumbersWithSum(self, array, tsum):
        # write code here
        if not array:
            return[]
        low,hight=0,len(array)-1
        while low<hight:
            total=array[low]+array[hight]
            if total>tsum:
                hight-=1
            elif total==tsum:
                return [array[low],array[hight]]
            else:
                low+=1
        return []
```

