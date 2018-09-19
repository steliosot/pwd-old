# Python Program for recursive binary search.
# Source: https://www.geeksforgeeks.org/binary-search/
# Returns index of key in arr if present, else -1
def binarySearch(arr, left, right, key):
    # Check base case
    if right >= left:

        mid = int(left + (right - left) / 2)

        # If element is present at the middle itself
        if arr[mid] == key:
            return mid

        # If element is smaller than mid, then it
        # can only be present in left subarray
        elif arr[mid] > key:
            return binarySearch(arr, left, mid - 1, key)

        # Else the element can only be present
        # in right subarray
        else:
            return binarySearch(arr, mid + 1, right, key)

    else:
        # Element is not present in the array
        return -1

# A helping function that prints index or a message that element does not exist
def binarySearchTester(alist, key):
    left, right = 0, len(alist)-1
    result = binarySearch(alist, left, right, key)
    if result ==-1:
        print("Element is not present in array")
    else:
        print("Element in array in index: ", result)


# Test array
arr = [2, 3, 4, 10, 40]
key = 12
binarySearchTester(arr,key)


