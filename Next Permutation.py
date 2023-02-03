class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if nums==[] or nums == None or len(nums)==1:
            return
        
        l = len(nums)-1
        i = l
        while (nums[i-1]>=nums[i] and i>0):
            i-=1
        
        if i==0:
            nums.sort()
            return 
        
        start = i-1
        last = l
        p = i-1
        next_to_start = i
     
        while p+1<=last:
            p+=1
            if nums[p] > nums[start] and nums[p] <= nums[next_to_start]:
                next_to_start = p
        nums[start],nums[next_to_start] = nums[next_to_start],nums[start]
        f = i
        b = l
        while f<=b:
            nums[f],nums[b] = nums[b],nums[f]
            f+=1
            b-=1
            
        return 
