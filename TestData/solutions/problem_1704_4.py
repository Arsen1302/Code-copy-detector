class Solution:
    def solution_1704_4(self, nums: List[int], space: int) -> int:
        d = dict()
        for n in nums:
            rem = n % space
            if rem in d:
                if n < d[rem][1]:
                    d[rem][1] = n
                d[rem][0] -= 1
            else:
                d[rem] = [-1, n]
        return min(d.values())[1]