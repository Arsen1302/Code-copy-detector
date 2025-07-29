class Solution:
    def solution_161_5_1(self, nums: List[int], lower: int, upper: int) -> int:
        def solution_161_5_2(l,r):
            if l > r:
                return 0
            m = (l+r)//2
            left = [0]
            s = 0
            for i in range(m-1,l-1,-1):
                s += nums[i]
                left.append(s)
            right = [0]
            s = 0
            for i in range(m+1,r+1):
                s += nums[i]
                right.append(s)
            right.sort()
            ans = 0
            for i in left:
                ans += (bisect.bisect_right(right,upper-i-nums[m]) - bisect.bisect_left(right,lower-i-nums[m]))
            return ans + solution_161_5_2(l,m-1)+solution_161_5_2(m+1,r)
        return solution_161_5_2(0, len(nums)-1)