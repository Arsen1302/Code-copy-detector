class Solution:
    def solution_1614_5(self, amount: List[int]) -> int:
        pq = [-x for x in amount]
        heapify(pq)
        ans = 0 
        while pq[0]: 
            x = heappop(pq)
            if pq[0]: heapreplace(pq, pq[0]+1)
            heappush(pq, x+1)
            ans += 1
        return ans