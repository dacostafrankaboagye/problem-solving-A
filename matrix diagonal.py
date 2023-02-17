# class Solution:
#     def diagonalSum(self, mat: List[List[int]]) -> int:
#         lp = 0
#         rp = len(mat)-1
#         rm = len(mat)%2
#         ans = 0

#         if rm ==0:
#             for m in mat:
#                 ans = ans + m[lp] + m[rp]
#                 lp +=1
#                 rp -=1
#             return ans

#         for m in mat:
#             if lp == rp and m[lp] == m[rp]:
#                 ans += m[lp]
#             else:
#                 ans = ans + m[lp] + m[rp]
#             lp +=1
#             rp -=1
#         return ans





class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        lp = 0
        rp = len(mat)-1
        rm = len(mat)%2
        ans = 0
        v =len(mat) // 2

       
        for m in mat:
            ans = ans + m[lp] + m[rp]
            lp +=1
            rp -=1
        if rm != 0:
            if v >0:
                ans-= mat[v][v]
                return ans
            else:
                return mat[0][0]
            
            

        return ans





