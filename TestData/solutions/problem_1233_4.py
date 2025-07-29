class Solution:
    def solution_1233_4(self, nums: List[int]) -> int:
        res = 0
        groups = collections.defaultdict(int)
        for num in nums:
            current = int(str(num)[::-1]) - num
            res += groups[current]
            groups[current] += 1
        
        return res % (10 ** 9 + 7)