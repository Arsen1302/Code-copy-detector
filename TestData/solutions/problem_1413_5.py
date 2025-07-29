class Solution:
    def solution_1413_5(self, n: int, quantities: List[int]) -> int:
        l, h = math.ceil(sum(quantities)/n), max(quantities)
		
        getCount = lambda x: sum(math.ceil(quantities[i]/x) for i in range(len(quantities)))
        while l < h:
            mid = l + (h - l)//2
			
			# if getting a low count than number of shops reduce the distribution
            if getCount(mid) <= n:
                h = mid
            else:
                l = mid + 1
                
        return l