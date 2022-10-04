from typing import List



class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        if k > len(arr): return arr
        # 原地实现快速排序
        def partition(array, low, high):
            # 返回值，初始化为 low + 1，用于记录分割点 index
            ret = low + 1
            check = array[low]
            # 从 low + 1 开始比较，比 check 低则与当前分割点交换，同时更新分割点
            for i in range(low + 1, high + 1):
                if array[i] < check:
                    array[i], array[ret] = array[ret], array[i]
                    ret += 1
            # 将 check 值与分割点前一个值进行交换，也就是小于 check 的最后一个值
            # 这样 check 值就在中间了，返回 ret - 1 为最终分割点 index
            array[low], array[ret - 1] = array[ret - 1], array[low]
            return ret - 1
        def quick_sort(array, low, high):
            if low > high: return
            index = partition(array, low, high)
            # if index == k: return
            quick_sort(array, low, index - 1)
            quick_sort(array, index + 1, high)
        quick_sort(arr, 0, len(arr) - 1)
        return arr[:k]

test = Solution()
arr = [2, 1, 4, 2, 6, 75, 21,0]
k = 6
# print(test.getLeastNumbers(arr, k))

# 实现一个归并排序, 据说是商汤常考
def mergesort(arr):
    n = len(arr)
    if n <= 1: return arr
    left= arr[:n // 2]
    right = arr[n // 2:]
    left = mergesort(left)
    right = mergesort(right)
    ret = []
    for i in range(n):
        if left and right:
            if left[0] < right[0]:
                ret.append(left.pop(0))
            else:
                ret.append(right.pop(0))
        elif left:
            ret.append(left.pop(0))
        elif right:
            ret.append(right.pop(0))
    return ret

print(mergesort(arr))