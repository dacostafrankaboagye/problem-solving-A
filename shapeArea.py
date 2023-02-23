'''
A 1-interesting polygon is just a square with a side of length 1. An n-interesting polygon is 
obtained by taking the n - 1-interesting polygon and appending 1-interesting polygons to its rim, 
side by side. You can see the 1-, 2-, 3- and 4-interesting polygons in the picture below.

'''

def solution(n):
    
    if n == 1:
        return 1
    temp = 1
    for i in range(1,n+1):
        temp = temp + (i*4 ) - 4
    return temp
