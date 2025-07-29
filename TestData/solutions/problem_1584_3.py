class Solution:
    def solution_1584_3(self, nums: List[int], k: int) -> int:
        heap = []
        count = 1
        
        for num in nums:
            heappush(heap, num)
            
        start = heappop(heap)
        
        while heap:
            num = heappop(heap)
            
            if num - start > k:
                start = num
                count += 1
                
        return count