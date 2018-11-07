# Append, set item, get item
# We just return a value (time is the same (or better we can say its almost the same)
# if we have 100, 1000, 10000 or 1B records)
# Complexity is always O(1)
def testO1(alist,position):
	return alist[position]

#print(testO1([1,2,3],2))

# Example of O(N), we search for the first item in the list
def testON(alist,element):
	for i in range(len(alist)):
		if(alist[i] == element):
			return i
	return -1

# Example of O(N), we search how many times an item exist in the list
def testONCount(alist,element):
	count = 0
	for i in range(len(alist)):
		if(alist[i] == element):
			count+=1
	return count

#print(testON([1,4,6],4))
print(testONCount([1,4,6,6,8,6,1,3,4,5],6))


# Example of O(N^2) (square)
# Search for the max values for each row of a matrix.
def testON2(alist):
	maxlist=[]
	for i in alist:
		max=0
		for j in i:
			if j > max:
				max =j
		maxlist.append(max)
	return maxlist

alist = [	[1,4,2],
			[4,8,5],
			[1,7,1]]

#print(testON2(alist))

# Matrix multiplication example of complexity O**3
# https://en.wikipedia.org/wiki/Matrix_multiplication

def matrixmult (A, B):
    rowsA, rowsB = len(A),len(B)
    colsA, colsB = len(A[0]),len(B[0])
    #print(rows_A,cols_A,rows_B,cols_B)
    if colsA != rowsB:
      print("Cannot multiply the two matrices. Incorrect dimensions.")
      return

    # Create the result matrix
    # Dimensions would be rowsA x colsB
    # Initialize with zeros!
    result = [[0 for row in range(colsB)] for col in range(rowsA)]
    print(result)

    for i in range(rowsA):
    	for j in range(colsB):
    		for k in range(colsA):
    			print(j, A[i][k],B[k][j]  )
    			result[i][j] += A[i][k] * B[k][j]

    return(result)
    
    
print(matrixmult([[1,2,3],[4,5,6]], [[7,8],[9,10],[11,12]]))    