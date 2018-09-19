import random as rand
import time as time
def generateKey(data,base,N,MAX):
    segment = data[N - 1] - data[0]
    randkey = data[0] + int(rand.random() * segment)
    return randkey

def generateArray(N,base, MAX):
    data=[]
    for _ in range(N):
        nextel = base + int(rand.random() * MAX)  # they keep growing!
        data.append(nextel)
        base = nextel
    return data

def binarySearchTester(alist, key):
    left, right = 0, len(alist)-1
    result = binarySearch(alist, left, right, key)
    if result ==-1:
        print("Element is not present in array")
    else:
        print("Element in array in index: ", result)

def benchmarkBinarySearch(N, base, MAX):
    mylist = generateArray(N,base, MAX)
    randkey = generateKey(mylist,base,N,MAX)
    start = time.time()
    result = binarySearch(mylist, 0, N, randkey)
    elapsed = time.time()-start
    return {"list":mylist, "key":randkey, "result":result, "elapsed":elapsed}


data = benchmarkBinarySearch(20,0,2)

print("My list: ", data['list'])
print("Key ",data['key'], " found at " ,data['result'] if data['result']!=-1 else "Key does not exist")

