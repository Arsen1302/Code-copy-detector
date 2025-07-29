class Solution:
    def solution_1712_4(self, costs: List[int], k: int, candidates: int) -> int:
        output = 0
        heap = []
        
        l, r = 0, len(costs) - 1
        j = candidates
        while l <= r and j:
            heapq.heappush(heap, (costs[l], l))
            # If l and r point to the same cell in costs don't push it twice
            if l != r:
                heapq.heappush(heap, (costs[r], r))
            l += 1
            r -= 1
            j -= 1

        while k:
            val, idx = heapq.heappop(heap)
            output += val
            if l <= r:
                # After every hire a new spot in the hiring pool opens we need to fill
                # We must figure out if the last candidate that was popped was from the left side
                # or the right side
                if abs(idx - l) <= abs(idx - r):
                    heapq.heappush(heap, (costs[l], l))
                    l += 1
                else:
                    heapq.heappush(heap, (costs[r], r))
                    r -= 1
        
            k -= 1
            
        
        return output