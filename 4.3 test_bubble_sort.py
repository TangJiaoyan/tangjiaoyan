#3 test_bubble_sort
import random


def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(1, len(arr)-i):
            if arr[j - 1] >= arr[j]:
                arr[j - 1], arr[j] = arr[j], arr[j - 1]


def test_bubble_sort():
    nums = random.sample(range(10), 10)
    x = 1
    nums.extend(random.sample(range(10),3))
    print(str(nums))
    bubble_sort(nums)
    print(str(nums))
    for i in range(len(nums)):
        for j in range(1, len(nums)-i):
            if nums[j - 1] <= nums[j]:
                x = 0
                assert x == 0
