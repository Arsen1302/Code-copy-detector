class Solution:
    def solution_1520_5(self, nums: List[int]) -> int:
        pq = [-x for x in nums]
        heapify(pq)
        sm = ss = sum(nums)
        ans = 0 
        while sm > ss/2: 
            ans += 1
            x = heappop(pq)
            sm -= -x/2
            heappush(pq, x/2)
        return ans