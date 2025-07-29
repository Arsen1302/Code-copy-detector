class Solution:
    def solution_161_3(self, nums: List[int], lower: int, upper: int) -> int:
        from sortedcontainers import SortedList
        l = SortedList()
        l.add(0)

        total = 0
        count = 0
        for v in nums:
            total += v
            count += (l.bisect_right(total - lower) - l.bisect_left(total - upper))
            l.add(total)
        
        return count