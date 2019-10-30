# coding=utf-8
"""
汉诺塔问题，把在a柱子上的n个盘子通过b柱子都移动c柱子上，分为三步
1、把a柱子的n-1个盘子通过c柱移动到b柱上
2、把第n个盘子移动到c柱子上
3、最后把b柱子的n-1个盘子通过a柱移动到c柱子上
"""

COUNT=0
def hanota(n, a, b, c):
    if n > 0:
        hanota(n - 1, a, c, b)
        #print('把%s柱子上的一个盘子移动到%s柱子上' % (a, c))
        global COUNT
        COUNT+=1
        hanota(n - 1, b, a, c)

if __name__ == '__main__':
    count=0
    hanota(20, 'A', 'B', 'C')
    print('盘子需要移动%s次'%COUNT)
