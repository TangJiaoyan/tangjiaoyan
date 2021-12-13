def linear_search(arr,x):
 
    n = len(arr)
    for i in range(n):
        if x == arr[i]:
            return i
    return -1
 
arr = ['3','5','2','9','6','1','8','7']
x = '2'
 
result = linear_search(arr,x)
 
if result == -1:
    print('there no this value')
else:
    print('the index is ',result)
