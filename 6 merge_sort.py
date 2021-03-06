#6 merge_sort
import random

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    middle = int(len(arr) / 2)

    left = arr[:middle]
    right = arr[middle:]

    left_data = merge_sort(left)
    right_data = merge_sort(right)

    return merge(left_data, right_data)


def merge(left, right):
    c = []
    l = len(left)
    r = len(right)

    l_start = 0
    r_start = 0

    while l_start < l and r_start < r:
        if left[l_start] <= right[r_start]:
            c.append(left[l_start])
            l_start += 1
        else:
            c.append(right[r_start])
            r_start += 1

    if l >= l_start:
        c.extend(left[l_start:])

    if r >= r_start:
        c.extend(right[r_start:])
    return c
if __name__ == "__main__":
    array = random.sample(range(10), 10)
    array.extend(random.sample(range(10), 3))
    print(array)
    merge_sort(array)
    print(array)


