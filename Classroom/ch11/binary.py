import numpy as np 
def binarySearch(data,key):
    data.sort()
    low = 0
    high = len(data)-1
    while low <= high:
        mid = (low+high)//2
        if data[mid] == key:
            return mid
        elif data[mid] < key:
            low = mid+1
        else:
            high = mid-1
    return -1
data=np.random.randint(1,50,10)
print(data)
key=int(input("enter the key you want to search"))
print(binarySearch(data,key))
