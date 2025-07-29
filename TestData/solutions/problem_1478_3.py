class Solution:
    def solution_1478_3(self, nums: List[int]) -> List[int]:
        freq = dict()
        result = []
        
        for n in nums:
            freq[n] = freq.get(n, 0) + 1
            
        for n in nums:
            if freq.get(n - 1, 0) == 0 and freq.get(n, 0) == 1 and freq.get(n + 1, 0) == 0:
                result.append(n)
        
        return result