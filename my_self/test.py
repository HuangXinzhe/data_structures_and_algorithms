def merge(left_arr, right_arr):
    result = []
    while left_arr and right_arr:
        if left_arr[0] < right_arr[0]:
            result.append(left_arr.pop(0))
        else:
            result.append(right_arr.pop(0))
    if left_arr:
        result += left_arr
    if right_arr:
        result += right_arr
    return result


def merge_sort(arr):
    if len(arr) < 2:
        return arr
    middle = len(arr) // 2
    left_arr = merge_sort(arr[:middle])
    right_arr = merge_sort(arr[middle:])
    return merge(left_arr, right_arr)


print(merge_sort([3, 2, 1, 4, 5]))
