class Solution:
    def solution_856_5(self, n: int) -> List[int]:
        if n % 2 == 1:
            res = [0]
        else:
            res = []
        i = 1
        while len(res) != n:
            res = [-i] + res
            res.append(i)
            i += 1
        return res