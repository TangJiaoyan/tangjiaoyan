#5 test_quick_sort
import random

def quick_sort(rank,left,right):

    base=rank[left]
    l=left
    h=right
    while l<h:
        while l< h:
            if rank[h]<base:
                rank[h],rank[l]=rank[l],rank[h]
                l+=1
                break
            else:
                h=h-1

        while l<h:
            if rank[l]>base:
               rank[l],rank[h]=rank[h],rank[l]
               h=h-1
               break
            else:
                l+=1
    if l<=left:
        pass
    else:
        quick_sort(rank,left,l-1)
    if h>=right:
        pass
    else:
        quick_sort(rank,h+1,right)


def test_quick_sort():
    nums = random.sample(range(10), 10)
    x = 1
    nums.extend(random.sample(range(10), 3))
    print(nums)
    quick_sort(nums, 0, len(nums) - 1)
    print(nums)
    for i in range(len(nums)):
        for j in range(1, len(nums) - i):
            if nums[j - 1] <= nums[j]:
                x = 0
                assert x == 0


