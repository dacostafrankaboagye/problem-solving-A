
def adjacent_num_product(list_nums):
   return max(a*b for a, b in zip(list_nums, list_nums[1:]))

def solution(inputArray):
    theMax = inputArray[0] * inputArray[1]
    
    for i in range(len(inputArray)-1):
        temp = inputArray[i] * inputArray[i+1]
        theMax = max(theMax, temp)
        
    print(theMax)
    
solution( [3, 6, -2, -5, 7, 3])
