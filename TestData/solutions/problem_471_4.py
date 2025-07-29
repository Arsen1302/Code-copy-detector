class Solution:
    def solution_471_4(self, answers: List[int]) -> int:
        d = defaultdict(int)
        for i in answers:
            d[i] += 1
        res = 0
        for i in d:
            res += ceil(d[i] / (i+1)) * (i+1)
        return res