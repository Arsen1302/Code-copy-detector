class Solution:
    def solution_1496_5(self, finalSum: int) -> List[int]:
        if finalSum % 2:
            return []
        res = []
        n = 2
        while finalSum >= 2*n + 2:
            res.append(n)
            finalSum -= n
            n += 2
            
        res.append(finalSum)
        return res