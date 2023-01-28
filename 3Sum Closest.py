
'''
Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.

 

Example 1:

Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
Example 2:

Input: nums = [0,0,0], target = 1
Output: 0
Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).
 

Constraints:

3 <= nums.length <= 500
-1000 <= nums[i] <= 1000
-104 <= target <= 104
'''



class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:

        '''
        since one solution is guaranteed - 
            temp = arr[0] + arr[1] + arr[lastElement]
        sort them
        loop through the arr
            two pointers
            while the left pointer(start) < right pointer(end)
               add the elements of the pointer , with the index pointer - 3 numbers
               if the sum < target
                    increase the left pointer
                if the sum > target 
                    reduce the right pointer
                if absolute(sum - target) < absolute(result - target)
                    result = the sum

        '''
        temp = nums[0] + nums[1] + nums[len(nums)-1]
        if len(nums) == 3:
            return temp
        nums = sorted(nums)
        for i in range(len(nums)-2):
            start = i+1
            end = len(nums)-1
            while start < end:
                theSum = nums[i] + nums[start] + nums[end]
                if theSum < target:
                    start +=1
                else:
                    end -=1
                if abs(theSum - target) < abs(temp - target):
                    temp = theSum
        return temp
        



                    







