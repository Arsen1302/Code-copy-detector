class Solution:
    def solution_365_4(self, nums: List[List[int]]) -> List[int]:
        k = len(nums)
        
        # reverse each list so we can pop lowest item from them
        for stack in nums: stack.reverse() 
            
        low,high = float('-inf'),float('inf')
            
        counts = defaultdict(int) # tracks num elements from each list
        queue = deque() # tracks current range
        
        # create heap / pq
        heap = []
        for i,stack in enumerate(nums):
            heapq.heappush(heap,(stack.pop(),i))
            
        while heap:
            num,i = heapq.heappop(heap)
            
            if nums[i]: heapq.heappush(heap, (nums[i].pop(),i))
            queue.append((num,i))
            counts[i] += 1
            
            # remove lowest items that we can afford to remove
            while len(counts) == k and counts[queue[0][1]] > 1:
                _, j = queue.popleft()
                counts[j] -= 1
                
            # interval comparison
            if len(counts) == k and queue[-1][0]-queue[0][0] < high-low:
                low,high= queue[0][0],queue[-1][0]
                    
            
        return [low,high]