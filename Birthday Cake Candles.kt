/*


You are in charge of the cake for a child's birthday. You have decided the cake will have one candle for each year of their total age. They will only be able to blow out the tallest of the candles. Count how many candles are tallest.

Example


The maximum height candles are  units high. There are  of them, so return .

Function Description

Complete the function birthdayCakeCandles in the editor below.

birthdayCakeCandles has the following parameter(s):

int candles[n]: the candle heights
Returns

int: the number of candles that are tallest
Input Format

The first line contains a single integer, , the size of .
The second line contains  space-separated integers, where each integer  describes the height of .

Constraints

Sample Input 0

4
3 2 1 3
Sample Output 0

2
Explanation 0

Candle heights are . The tallest candles are  units, and there are  of them.


*/


fun birthdayCakeCandles(candles: Array<Int>): Int {
    // Write your code here
    // what of [2,1,7,1,7,7,2,10,9,10,10,0, 9, 10]
    var theMax = 0
    var ans = 0
    for(i in candles){
        if(theMax < i){
            ans = 0
        }
        theMax = max(theMax, i)
        if(theMax == i){
            ans +=1
        }
 
    }
    return ans

}










