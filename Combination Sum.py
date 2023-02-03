class Solution:
    def combinationSum(self, A: List[int], B: int) -> List[List[int]]:
        ans = []
        A.sort()
        
        def solve(ind=0,curr_sum=0,curr_list=[]):
            if curr_sum==B:
                if curr_list not in ans:
                    ans.append(curr_list[:])
                return
            for i in range(ind,len(A)):
                if curr_sum+A[i]>B:
                    break
                solve(i,curr_sum+A[i],curr_list+[A[i]])
        
        solve()
        return ans
        
