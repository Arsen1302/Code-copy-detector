class Solution:
    def solution_1134_5(self, nums: List[int], k: int) -> int:
        freq = {}
        for x in nums: freq[x] = 1 + freq.get(x, 0)
        
        ans = 0
        for x, v in freq.items(): 
            if k - x in freq: 
                if x == k - x: ans += freq[x]//2
                elif x < k - x: ans += min(freq[x], freq[k-x])
        return ans