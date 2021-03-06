#!/usr/bin/python3
# -*- coding: utf-8 -*-


import cProfile
import random

from quick_sort import quick_sort   # 导入自己编写的快速排序模块,感觉挺奇妙的


def binary_search(arr, n):
    """middle_index +/-1 造成两次死循环"""

    if isinstance(arr, list) and isinstance(n, (int, float)):
        length = len(arr)
        # if length == 0:
        #     return 'list is empty'
        # if length == 1 and arr[0] == n:
        #     return 0
        left_index = 0
        right_index = length - 1
        while left_index <= right_index:
            middle_index = left_index // 2 + right_index // 2
            if arr[middle_index] == n:
                return middle_index
            elif arr[middle_index] < n:
                left_index = middle_index + 1
            else:
                right_index = middle_index - 1
        # binary_search(arr[left_index:right_index],n)
        return 'no this number'
    else:
        raise TypeError('type of input is error')


if __name__ == '__main__':

    # 测试函数: binary_search()
    arr = []
    for i in range(1000):
        arr.append(random.randint(1, 300))
    for x in range(3):
        random.shuffle(arr)
    arr = quick_sort(arr)
    n = random.randint(1, 300)
    # arr = [99]
    # n = 999
    result_index = binary_search(arr, n)
    print(result_index)
    cProfile.run('binary_search(arr, n)')
