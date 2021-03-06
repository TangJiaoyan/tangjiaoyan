#1 test_selection_sort
import random


def selection_sort(arr):
    for i in range(len(arr)):
        min_indx = i
        for j in range(i, len(arr)):
            if arr[j] < arr[min_indx]:
                min_indx = j
        arr[i], arr[min_indx] = arr[min_indx], arr[i]


def test_selection_sort():
    nums = random.sample(range(10), 10)
    x = 1
    nums.extend(random.sample(range(10),3))
    print(str(nums))
    selection_sort(nums)
    print(str(nums))
    for i in range(len(nums)):
        for j in range(1, len(nums) - i):
            if nums[j - 1] <= nums[j]:
                x = 0
            else:
                x = 1
                break
    assert x == 0
