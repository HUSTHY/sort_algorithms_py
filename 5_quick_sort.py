def quick_sort(arr,simulation):
    """
    快速排序(quick sort)的采用了分治的策略。
    分治策略指的是：
    将原问题分解为若干个规模更小但结构与原问题相似的子问题。递归地解这些子问题，然后将这些子问题的解组合为原问题的解。
    快排的基本思想是：
    在序列中找一个划分值，通过一趟排序将未排序的序列排序成 独立的两个部分，其中左边部分序列都比划分值小，右边部分的序列比划分值大，此时划分值的位置已确认，然后再对这两个序列按照同样的方法进行排序，从而达到整个序列都有序的目的。

    :param arr:
    :param simulation:
    :return:
    """
    iteration = 0
    if simulation:
        print("iteration", iteration, ":", *arr)
    arr, _ = q_sort(arr, 0, len(arr) - 1, iteration, simulation)
    return arr


def q_sort(arr,left,right,iteration,simulation):
    if left < right:
        #得到基准值的index
        povit_index = partion(arr,left,right)

        if simulation:
            iteration += 1
            print("iteration", iteration, ":", *arr)

        _, iteration = q_sort(arr,left,povit_index-1,iteration,simulation)
        _, iteration = q_sort(arr,povit_index+1,right,iteration,simulation)
    #跳出递归
    return arr,iteration

def partion(arr,left,right):
    """
    分治策略，把小于基准值的放在左边集合，大于基准值的放在右边，基准值放在中间
    这里就是在原list上操作的，没有额外的申请空间
    :param arr:
    :param left:
    :param right:
    :return: left 基准值排序后正确的索引位置
    """
    #这里是把list的第一个值作为基准值的
    pivot = arr[left]#基准值


    while left< right:
        #从右往左找，如果出现比基准小的就跳出循环，arr[left] = arr[right]实现了把这个小值的放在左边，抽象为小值list集合
        while left< right and arr[right]>= pivot:
            right -= 1
        arr[left] = arr[right]

        #从左往右找，如果出现比基准大的就跳出循环，arr[right] = arr[left]实现了把这个大值的放在右边，抽象为大值list集合
        while left < right and arr[left] <= pivot:
            left += 1
        arr[right] = arr[left]

        #把基准值放在中间去
        arr[left] = pivot
    return left

if __name__ == '__main__':
    arr = [10, 2, 5, 1, 3, 7, 3, 1525, 0]
    print(arr)
    arr = quick_sort(arr, True)
    print(arr)