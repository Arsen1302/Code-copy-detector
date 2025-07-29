class Solution:
    def solution_969_1(self, n: int) -> List[str]:
        if n == 1:
            return []
        else:
            numerator = list(range(1,n))
            denominator = list(range(2,n+1))
            res = set()
            values = set()
            for i in numerator:
                for j in denominator:
                    if i < j and i/j not in values:
                        res.add(f'{i}/{j}')
                        values.add(i/j)
            return res