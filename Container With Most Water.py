class Solution:
    def maxArea(self, h: List[int]) -> int:
        s = 0
        e = len(h)-1

        max_area =0

        while s<e:
            max_area = max(max_area,min(h[s],h[e])*abs(e-s))
            if h[s]>h[e]:
                 e-=1
            else:
                s+=1
        return max_area
