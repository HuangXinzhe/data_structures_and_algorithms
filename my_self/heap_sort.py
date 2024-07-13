# 小顶堆找到最大的k个数
def heap_sort(nums, k):
    def sift_down(start, end):
        root = start
        while True:
            child = 2 * root + 1
            if child > end:
                break
            if child + 1 <= end and nums[child] > nums[child + 1]:
                child += 1
            if nums[root] > nums[child]:
                nums[root], nums[child] = nums[child], nums[root]
                root = child
            else:
                break

    for i in range((len(nums) - 2) // 2, -1, -1):
        sift_down(i, len(nums) - 1)

    for i in range(len(nums) - 1, len(nums) - k - 1, -1):
        nums[0], nums[i] = nums[i], nums[0]
        sift_down(0, i - 1)

    return nums[-k:]