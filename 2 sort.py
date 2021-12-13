#1 selection_sort
import random


def selection_sort(arr):
    for i in range(len(arr)):
        min_indx = i
        for j in range(i, len(arr)):
            if arr[j] < arr[min_indx]:
                min_indx = j
        arr[i], arr[min_indx] = arr[min_indx], arr[i]


if __name__ == '__main__':
    nums = random.sample(range(10), 10)
    nums.extend(random.sample(range(10),3))
    print(str(nums))
    selection_sort(nums)
    print(str(nums))
    


    
 #2 insertion_sort
import random


def insertion_sort(arr):
    for i in range(len(arr)):
        val = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > val:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = val



if __name__ == '__main__':
    nums = random.sample(range(10), 10)
    nums.extend(random.sample(range(10),3))
    print(str(nums))
    insertion_sort(nums)
    print(str(nums))
    
    
        
#3 bubble_sort
import random


def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(1, len(arr)-i):
            if arr[j - 1] >= arr[j]:
                arr[j - 1], arr[j] = arr[j], arr[j - 1]


if __name__ == '__main__':
    nums = random.sample(range(10), 10)
    nums.extend(random.sample(range(10),3))
    print(str(nums))
    bubble_sort(nums)
    print(str(nums))
