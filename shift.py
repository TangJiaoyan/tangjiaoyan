#1
#time complexity = O(1)
#Space Complexity = O(1)
if __name__ == "__main__":
    n=8
    m=3 
    def move(arr,n,m):
      arr_end=arr[n-1]
      for i in range(n-1,-1,-1):
        arr[i]=arr[i-1]
      arr[0]=arr_end
      m-=1
      if m>0:move(arr,n,m)


for i in range(n) :
 number=['3','5','6','10','9','1','2','0']
move(number,n,m)
print,number

#2
#Time Complexity = O(n)
#Space Complexity = O(1)
def reverse(arr,start,end):
    while start<end:
        temp = arr[start]
        arr[start] = arr[end]
        arr[end] = temp
        start += 1
        end -= 1
 
def rightShift(arr,k):
    lens = len(arr)
    k %= lens
    reverse(arr,0,lens-k-1)
    reverse(arr,lens-k,lens-1)
    reverse(arr,0,lens-1)
 
if __name__ == "__main__":
    k = 3
    arr = ['3','5','6','10','9','1','2','0']
    rightShift(arr,k)
    i = 0
    while i < len(arr):
        print(arr[i],end=" ")
        i += 1

#3
#time complexity = O(n)
#Space Complexity = O(1)
def rightShift(arr,k):
    lens = len(arr)
    k %= lens 
    while k != 0:
        tmp = arr[lens-1] 
        i = lens-1
        while i > 0:
            arr[i] = arr[i-1] 
            i -= 1
        arr[0] = tmp
        k -= 1
 
if __name__ == "__main__":
    k = 3
    arr = ['3','5','6','10','9','1','2','0']
    rightShift(arr,k)
    i = 0
    while i < len(arr):
        print(arr[i],end=" ")
        i += 1
