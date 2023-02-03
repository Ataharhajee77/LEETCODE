class Solution:
    def trap(self, A: List[int]) -> int:
        water = 0
        left = 0
        right = len(A)-1

        left_biggest_wall = 0
        right_biggest_wall = 0

        while left < right:
            if A[left] < A[right]:
                left_biggest_wall = max(left_biggest_wall,A[left])
                if A[left] < left_biggest_wall:
                    water += left_biggest_wall-A[left]
                left +=1

            else:
                right_biggest_wall = max(right_biggest_wall,A[right])
                if A[right] < right_biggest_wall:
                    water += right_biggest_wall-A[right]
                right-=1

        return(water)
