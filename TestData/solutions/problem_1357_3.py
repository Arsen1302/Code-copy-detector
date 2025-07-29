class Solution:
    def solution_1357_3(self, nums: List[str], k: int) -> str:
        pq = [] # min-heap 
        for x in nums: 
            heappush(pq, int(x))
            if len(pq) > k: heappop(pq)
        return str(pq[0])