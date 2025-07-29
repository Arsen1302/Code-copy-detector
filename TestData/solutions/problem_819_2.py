class Solution:
    def solution_819_2(self, nums: List[int], k: int) -> int:
        odd_ls = []
        for i, num in enumerate(nums):
            if num % 2 == 1:
                odd_ls.append(i)
                
        odd_ls = [-1] + odd_ls + [len(nums)]
        count = 0
        for i in range(1, len(odd_ls) - k):
            count += (odd_ls[i] - odd_ls[i - 1]) * (odd_ls[i + k] - odd_ls[i + k - 1])
        
        return count