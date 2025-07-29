class Solution:
    
    def solution_996_3_1(self, blooms, days, m, k):
        flowers = 0
        for flower in blooms:
            flowers = flowers + 1 if (flower <= days) else 0
            if flowers == k:
                m -= 1
                flowers = 0
        return m <= 0
    
    def solution_996_3_2(self, bloomDay: List[int], m: int, k: int) -> int:
        if len(bloomDay) < m * k: return -1
        left, right = 1, max(bloomDay)
        while left < right:
            mid = (left + right) // 2
            if self.solution_996_3_1(bloomDay, mid, m, k):
                right = mid
            else:
                left = mid + 1
        return left