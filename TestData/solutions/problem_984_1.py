class Solution:
    def solution_984_1(self, nums: List[int]) -> int:
        # approach 1: find 2 max numbers in 2 loops. T = O(n). S = O(1)
		# approach 2: sort and then get the last 2 max elements. T = O(n lg n). S = O(1)
		# approach 3: build min heap of size 2. T = O(n lg n). S = O(1)
		# python gives only min heap feature. heaq.heappush(list, item). heapq.heappop(list)
        
        heap = [-1]
        for num in nums:
            if num > heap[0]:
                if len(heap) == 2:
                    heapq.heappop(heap)
                heapq.heappush(heap, num)
                
        return (heap[0]-1) * (heap[1]-1)