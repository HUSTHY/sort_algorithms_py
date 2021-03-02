def insertion_sort(arr,simulation = False):
    """
    插入排序
    原理——是通过构建有序序列，对于未排序数据，在已排序序列中从后向前扫描，找到相应位置并插入
    Complexity: O(n^2)
    :param arr:
    :param simulation:
    :return:arr
    稳定
    """
    iteration = 0
    if simulation:
        print('Iteration',iteration,':',*arr)

    for i in range(len(arr)):
        cursor = arr[i]
        index = i #记住该索引，把这个索引对应的元素和前面的进行比较。

        #如果前面的元素有比cursor大的，就把该元素和后面一个元素替换位置
        while index > 0 and arr[index-1] > cursor:
            arr[index] = arr[index-1]
            index -= 1
        arr[index] = cursor
        if simulation:
            iteration += 1
            print('Iteration',iteration,':', *arr)

    return arr

if __name__ == '__main__':
    arr = [10, 2, 5, 1, 3, 7, 3, 1525, 0]
    print(arr)
    arr = insertion_sort(arr, True)
    print(arr)