class Solution:
    def solution_992_2(self, arr: List[int], target: int) -> int:
        n = len(arr)
        heap = []
        prefix_sum = {}
        prefix_sum[0] = -1
        curr_sum = 0
        for i in range(n): 
            curr_sum += arr[i]
            if prefix_sum.get(curr_sum - target):
                heapq.heappush(heap,(i - prefix_sum.get(curr_sum - target), i))
            prefix_sum[curr_sum] = i
                
        while len(heap) > 1:
            len1, end1 = heapq.heappop(heap)
            len2, end2 = heapq.heappop(heap)
            if end1 <= end2 - len2 or end2 <= end1 - len1:    
                return len1 + len2
            else:    # overlap
                heapq.heappush(heap, (len1, end1))
                
        return -1