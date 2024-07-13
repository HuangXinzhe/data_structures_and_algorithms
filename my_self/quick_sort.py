input_str = "Ihave1nose2hands10fingers"
input_list = [int(ord(x)) for x in input_str]


def partition(arr, low, high):
    i = low - 1
    pivot = arr[high]
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[j], arr[i] = arr[i], arr[j]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1


def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi-1)
        quick_sort(arr, pi+1, high)
    return arr


result = quick_sort(input_list, 0, len(input_list)-1)

result_str = ""
for r in result:
    result_str += chr(r)
print(result_str)
