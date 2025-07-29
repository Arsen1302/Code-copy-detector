class Solution:
    def solution_1125_1_1(self, tasks: List[List[int]]) -> int:
        tasks.sort(key=lambda x: x[0]-x[1])
        def solution_1125_1_2(mid):
            for actual, minimum in tasks:
                if minimum > mid or actual > mid: return False
                if minimum <= mid: mid -= actual
            return True
        l, r = 0, 10 ** 9
        while l <= r:
            mid = (l+r) // 2
            if solution_1125_1_2(mid): r = mid - 1
            else: l = mid + 1
        return l