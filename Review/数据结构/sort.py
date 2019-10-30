# coding=utf-8

# 改进冒泡排序，如果某一趟结束后，顺序不变，证明已经排序好了，就不用继续往下排序了
def bubble_sort(array):
    for i in range(len(array) - 1):
        exchange = False
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                exchange = True
        # print(array)
        if not exchange:
            break


def select_sort(array):
    """
    选择排序：
    基本思想：第一趟，在待排序记录r1—r[n]中选出最小的记录；将它与r1交换；
    第2趟，在待排序记录r2 ~ r[n]中选出最小的记录，将它与r2交换；以此类推，
    第i趟在待排序记录r[i] ~ r[n]中选出最小的记录，将它与r[i]交换，
    使有序序列不断增长直到全部排序完毕。
    """
    for i in range(len(array) - 1):
        min_index = i
        for j in range(i + 1, len(array)):
            if array[j] < array[min_index]:
                min_index = j
        if min_index != i:
            array[i], array[min_index] = array[min_index], array[i]
        # print(array)


def insert_sort(array):
    """
        插入排序：
        默认序列中的第0个元素是有序的（因为只有一个元素a[0]嘛，自然是有序的）；
        从下标为1（下标0没啥好插的）的元素开始，取当前下标i位置处的元素a[i]保存到一个临时变量waitInsert里；
        waitInsert与对前半部分有序序列的循环遍历比较，直到遇到第一个比waitInsert大的元素（这里默认是从小到大排序），此时的下标为j，然后将其插入到j的位置即可；
        因为前面的插入，导致后面元素向后推移一个位置，
    """
    for i in range(1, len(array)):
        tmp = array[i]
        j = i - 1
        while j >= 0 and array[j] > tmp:
            # 将数往后退
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = tmp
        # print(array)


def quick_sort(array, start, end):
    """
        快速排序：
        1. 先从数列中取出一个数作为基准数。
        2. 分区过程，将比这个数大的数全放到它的右边，小于或等于它的数全放到它的左边。
        3. 再对左右区间重复第二步，直到各区间只有一个数。

    """
    if start >= end:
        return
    mid = array[start]
    left = start
    right = end
    while left < right:
        while left < right and array[right] >= mid:
            right -= 1
        array[left] = array[right]
        while left < right and array[left] <= mid:
            left += 1
        array[right] = array[left]
    array[left] = mid
    quick_sort(array, start, left - 1)
    quick_sort(array, left + 1, end)


def heap_sort(array):
    """
    堆排序，先建大顶堆堆，每次都将堆顶和堆尾先交换位置，然后再调整堆
    :param array:
    :return:
    """
    n = len(array)

    def sift(array, low, high):
        """
        调整堆
        :param array:列表
        :param low:根节点的位置
        :param high:最后一个节点的高度
        :return:
        """
        i = low  # i最开始指向根节点
        tmp = array[low]  # 保存根节点的值
        j = 2 * i + 1  # j指向i的左孩子
        while j <= high:
            if j + 1 <= high and array[j + 1] > array[j]:  # 比较两个孩子的大小，指向数值较大的孩子
                j = j + 1
            if array[j] > tmp:  # 如果孩子比根节点值大，则将孩子往上移动，将i，j指针往下移
                array[i] = array[j]
                i = j
                j = 2 * i + 1
            else:
                break
        array[i] = tmp  # 将根节点放在合适的地方
        return array

    # 先建堆
    for i in range((n - 2) // 2, -1, -1):
        sift(array, i, n - 1)
    for i in range(n - 1, -1, -1):
        array[i], array[0] = array[0], array[i]
        sift(array, 0, i - 1)


array = [3, 6, 78, 34, 435, 14, 45]
print(array)
heap_sort(array)
print(array)
