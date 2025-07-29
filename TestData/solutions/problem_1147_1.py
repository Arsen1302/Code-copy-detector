class Solution:
    def solution_1147_1(self, nums: List[int], k: int) -> int:
        pq = [] # max heap 
        for i in reversed(range(len(nums))): 
            while pq and pq[0][1] - i > k: heappop(pq)
            ans = nums[i] - pq[0][0] if pq else nums[i]
            heappush(pq, (-ans, i))
        return ans