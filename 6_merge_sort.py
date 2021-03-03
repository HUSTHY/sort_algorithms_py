def merge_sort(arr):
    """
     Merge Sort
        Complexity: O(n log(n))
    归并排序算法，不断的把序列分割成长度相等的2部分，每个序列长度为1；
    然后不断的合并在一起。怎么合并？左右长度相等两个子序列从0开始比较，然后安装正确的顺序
    保存在新开辟的空间中。
    由于最小的淄川长度为1，所以归并后的序列一定是排序排好了的。
    :param arr:
    :return:
    """
    if len(arr)<=1:
        return arr
    mid = len(arr)//2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left,right)

def merge(left,right):
    merged = []
    i = 0
    j = 0
    while i<len(left) and j<len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged += left[i:]
    merged += right[j:]
    return merged

if __name__ == '__main__':
    arr = [10, 2, 5, 1, 3, 7, 3, 1525, 0]
    print(arr)
    arr = merge_sort(arr)
    print(arr)