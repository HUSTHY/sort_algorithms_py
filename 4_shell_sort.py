def shell_sort(arr,simulation):
    iteration = 0
    if simulation:
        print('Iteration',iteration,':',*arr)

    n = len(arr)
    gap = n//2
    while gap > 0:
        for  i in range(gap,n):

            temp = arr[i]
            index = i

            while index > 0 and arr[index-gap] >temp:
                arr[index] = arr[index-gap]
                index -= gap
            arr[index] = temp

        gap = gap//2
        if simulation:
            iteration += 1
            print('Iteration',iteration,':', *arr)

        gap = gap//2


    return arr

if __name__ == '__main__':
    arr = [10, 2, 5, 1, 3, 7, 3, 1525, 0]
    print(arr)
    arr = shell_sort(arr, True)
    print(arr)