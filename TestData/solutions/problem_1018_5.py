class Solution:
    def solution_1018_5(self, s: str) -> int:
        j = s.split('0')
        total = []
        for x in j:
            if x:
                k = len(x)
                total.append(((k)*(k+1))//2)

        return sum(total)%(10**9+7)