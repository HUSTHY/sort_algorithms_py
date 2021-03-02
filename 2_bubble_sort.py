def bubble_sort(arr,simulation=False):
    """
    Worst-case performance: O(N^2)
    冒泡排序
    思想——比较相邻的元素。如果第一个比第二个大，就交换他们两个。对每一对相邻元素做同样的工作，从开始第一对到结尾的最后一对。重复上面的操作！
    :param arr:
    :param simulation:
    :return:arr
    稳定的：如果a原本在b前面，而a=b，排序之后a仍然在b的前面。
    """
    iteration = 0
    if simulation:
        print("iteration", iteration, ":", *arr)
    length = len(arr)
    while length > 0:
        for i in range(length-1):
            if arr[i] > arr[i+1]:
                arr[i],arr[i+1] = arr[i+1],arr[i]

                # temp = arr[i]
                # arr[i] = arr[i+1]
                # arr[i+1] = temp
                if simulation:
                    iteration += 1
                    print("iteration", iteration, ":", *arr)
        length -= 1
    return arr

if __name__ == '__main__':
    arr = [10, 2, 5, 1, 3, 7, 3, 1525, 0]
    print(arr)
    arr = bubble_sort(arr, True)
    print(arr)