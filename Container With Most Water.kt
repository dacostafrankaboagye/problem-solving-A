/*

You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
Input: height = [1,1]
Output: 1



*/



// brute force way
// go throught for each single point and find the area - O(n^2)



import kotlin.math.min

class Solution {
    fun maxArea(height: IntArray): Int {
        // .. brute force approach
        var result = 0
        for(i in 0 until height.size){
            for(j in i+1 until height.size){
                var area = (j-i) * Math.min(height[i],height[j])  // length * height
                result = Math.max(result, area)
            }
        }
        return result
        
    }
}




// another approach - O(n)

/*

Use two pointers - left and right -> pointing to the first and last respectively
cal the area
update the pointer witht the smallest value


*/

import kotlin.math.min

class Solution {
    fun maxArea(height: IntArray): Int {
        // .efficent approach
        var result = 0
        var leftPointer = 0
        var rightPointer = height.size -1
        while(leftPointer != rightPointer){
            var theMinValue = Math.min(height[leftPointer], height[rightPointer])
            var area = (rightPointer- leftPointer) * theMinValue
            result = Math.max(result, area)
            if(height[leftPointer] <= height[rightPointer]){
                leftPointer +=1
            }else{
                rightPointer-=1
            }
        }
        return result
        
    }
}
























