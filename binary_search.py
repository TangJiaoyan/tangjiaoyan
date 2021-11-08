def binary_search(my_list, value):
    low = 0
    high = len(my_list) - 1
    while low <= high:
        mid = int((low + high) / 2)
        guess = my_list[mid]
        if guess < value:
            low = mid + 1
        if guess > value:
            high = mid - 1
        if guess == value:
            return mid
    return None


num_list = [2,5,8,12,16,23,38,56,72,91]
print(binary_search(num_list, 23))
