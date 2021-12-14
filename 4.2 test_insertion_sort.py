#2 test_insertion_sort

import random


def insertion_sort(arr):
    for i in range(len(arr)):
        val = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > val:
            arr[ j +1] = arr[j]
            j -= 1
        arr[ j +1] = val



def test_insertion_sort():
    nums = random.sample(range(10), 10)
    x = 1
    nums.extend(random.sample(range(10) ,3))
    print(str(nums))
    insertion_sort(nums)
    print(str(nums))
    for i in range(len(nums)):
        for j in range(1, len(nums) - i):
            if nums[j - 1] <= nums[j]:
                x = 0
            else:
                x = 1
                break
    assert x == 0
