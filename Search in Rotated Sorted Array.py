class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if nums==None or len(nums)==0:
            return -1
        
        l = 0
        r = len(nums)-1

        while l<r:
            m = l +(r-l)//2

            if nums[m]>nums[r]:
                l = m+1
            else:
                r=m

        start = l
        l = 0
        r = len(nums)-1

        if target>=nums[start] and target<=nums[r]:
            l = start
        else:
            r=start-1

        while(l<=r):
            m = l+(r-l)//2
            if nums[m]==target:
                return m
            elif target<nums[m]:
                r=m-1
            else :
                l=m+1
        return -1
        
