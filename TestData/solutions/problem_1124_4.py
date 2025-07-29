class Solution:
    def solution_1124_4(self, nums: List[int]) -> int:
        n = len(nums)
        left = [[] for i in range(n)]
        right = [[] for i in range(n)]
        even,odd,ans= [0]*3
        for i in range(n):
            left[i] = [even,odd]
            if i % 2 == 0:
                even+=nums[i]
            else:
                odd+=nums[i]
        even,odd = 0,0
        for i in range(n-1,-1,-1):
            right[i] = [even,odd]
            if i % 2 == 0:
                even+=nums[i]
            else:
                odd+=nums[i]
        for i in range(n):
            left_even_sum = left[i][0]
            left_odd_sum = left[i][1]
            right_even_sum = right[i][0]
            right_odd_sum = right[i][1]
            if left_even_sum + right_odd_sum == left_odd_sum + right_even_sum:
                ans+=1
        return ans