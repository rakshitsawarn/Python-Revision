def selection_sort(nums):
    n = len(nums)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if nums[j] < nums[min_index]:
                min_index = j
        nums[i], nums[min_index] = nums[min_index], nums[i]
    return nums
nums = [64, 25, 12, 22, 11]
sorted_nums = selection_sort(nums)
print("Sorted array:", sorted_nums)

