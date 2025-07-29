class Solution:
    def solution_1620_5(self, nums: List[int], numsDivide: List[int]) -> int:
        counts = list(Counter(nums).items())
        heapq.heapify(counts)        
        g = reduce(math.gcd, numsDivide)        
        
        result = 0
        while counts:
            if g % counts[0][0] == 0:
                return result
            
            _, cnt = heapq.heappop(counts)
            result += cnt
            
        return -1