class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return(self.rec(nums))
    def rec(self,lst):
        if len(lst)==0:
            return []
        elif len(lst)==1:
            return [lst]
        else:
            l = []
            for i in range(len(lst)):
                x = lst[i]
                y = lst[:i]+lst[i+1:]
                for p in self.rec(y):
                    l.append([x]+p)
            return l
