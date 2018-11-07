# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 12:28:34 2018

@author: stelios
"""
def linearSearch(alist, key): 
  
    for i in range(len(alist)): 
        if alist[i] == key: 
            return i 
    return -1


def linearSearch2D(alist,key):

    for row in alist:
        for element in row:
            if element == key:
                return element
    return -1


def linearSearch2DPositions(alist,key):
    count = 0
    pos = []
    for x in range(len(alist)):
        for y in range(len(alist)):
            if alist[x][y] == key:
                count +=1
                pos.append([x,y])
    return count, pos

mylist = [ [11,4,3], 
           [4,5,3], 
           [6,4,11]
         ]
key = 4
count, positions = linearSearch2DPositions(mylist,key)
print(count)
print(positions)

	
def bubbleSort(alist):
    for i in range(len(alist)):
        for j in range(0,len(alist)-i-1):
            if alist[j] > alist[j+1] :
                alist[j], alist[j+1] = alist[j+1], alist[j]
            """
            #Same as before
            if alist[i]>alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
            """