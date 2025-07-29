class Solution:
    def solution_283_3_1(self, left, right):
        i, j = 0, 0
        m, n = len(left), len(right)
        while i < m:
            while j < n and left[i] > 2*right[j]:
                j += 1
            self.ans += j
            i += 1
        
        i, j = 0, 0
        temp = []
        while i < m and j < n:
            if left[i] < right[j]:
                temp.append(left[i])
                i += 1
            else:
                temp.append(right[j])
                j += 1
        
        while i < m:
            temp.append(left[i])
            i += 1
        while j < n:
            temp.append(right[j])
            j += 1
        
        return temp
    
    def solution_283_3_2(self, nums):
        if len(nums) <= 1:
            return nums
        mid = len(nums) // 2
        left, right = self.solution_283_3_2(nums[:mid]), self.solution_283_3_2(nums[mid:])
        return self.solution_283_3_1(left, right)
    
    def solution_283_3_3(self, nums: List[int]) -> int:
        self.ans = 0
        _ = self.solution_283_3_2(nums)
        return self.ans