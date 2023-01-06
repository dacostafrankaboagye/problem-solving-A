/*

Given an integer x, return true if x is a 
palindrome
, and false otherwise.

 
 An integer is a palindrome when it reads the same forward and backward.

For example, 121 is a palindrome while 123 is not.

*/


class Solution {
    fun isPalindrome(x: Int): Boolean {
        var temp = x.toString()
        return temp == temp.reversed()
        
    }
}
