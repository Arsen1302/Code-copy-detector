class Solution:
    def solution_1520_3(self, nums: List[int]) -> int:
        res, max_heap, total, curr_total = 0, [], sum(nums), sum(nums)
        for n in nums:
            heappush(max_heap, -n)
        while max_heap:
            n = -heappop(max_heap)
            res += 1
            curr_total -= n / 2
            if curr_total <= total / 2:
                break
            heappush(max_heap, -n / 2)
        return res