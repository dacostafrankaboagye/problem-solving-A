'''

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters.


'''



'''

j = 0
        k = 0
        ans = ""
        for i in range(len(strs)):
            idx = strs[i][j]
            for m in strs:
                if m[i][j] == idx:
                    ans += m[i][j]
            j+=1


---

        temp =  strs[0]
        j =0
        count = 0
        ans  = ""
        while True:
            for i in strs:
                try:

                    if i[j] != temp[j]:
                        break
                    else:
                        count +=1
                        if count == len(strs):
                            ans += temp[j]
                            j +=1
                            count = 0
                except:
                    break
        if count == 3:
            return ans
        return ""
                

'''


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        minStr = min(strs, key=len)
        ans = ""
        idx = 0
        for i in list(minStr):
            for j in strs:
                if i != j[idx]:
                    return ans
            ans += i
            print(ans)
            idx +=1
        return ans


                    
            
            

        

