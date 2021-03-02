def selection_sort(arr,simulation=False):
    """
    election Sort
    Complexity: O(n^2)
    思想：每一趟选择出最小的那个元素，然后把它放在最前面或者最后面
    :param arr: 排序前的数组
    :param simulation: 是否模拟算法过程
    :return: arr: 排序后的数组
    不稳定：如果a原本在b的前面，而a=b，排序之后 a 可能会出现在 b 的后面。
    """
    iteration = 0
    if simulation:
        print("iteration", iteration, ":", *arr)

    for i in range(len(arr)):
        min_index = i
        for j in range(i+1,len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[min_index],arr[i] = arr[i],arr[min_index]

        # temp = arr[min_index]
        # arr[min_index] = arr[i]
        # arr[i] = temp

        if simulation:
            iteration += 1
            print("iteration", iteration, ":", *arr)

    return arr

if __name__ == '__main__':
    arr = [10, 2, 5, 1, 3, 7, 3,1525,0]
    print(arr)
    arr = selection_sort(arr,True)
    print(arr)
