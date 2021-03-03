
def counting_sort(arr):
    """
    计数排序，先找出序列中的最大值和最小值，新建一个list统计每个值出现的次数；然后把这个list的值重新赋值给arr来进行排序
    :param arr:
    :return:
    """
    max = arr[0]
    min = arr[0]
    for ele in arr:
        if ele < min:
            min = ele
        if ele>max:
            max = ele
    count = [0]*(max-min+1)

    #计数
    for ele in arr:
        count[ele-min]+=1

    #填值
    index = 0
    for i in range(len(count)):
        #count[i] = 0 for循环就不会执行
        for ele in range(count[i]):
            arr[index] = i+min
            index += 1

    print(*arr)




if __name__ == '__main__':
    arr = [10, 2, 5, 1, 3, 7, 3, 1525, 0]
    print(arr)
    counting_sort(arr)

