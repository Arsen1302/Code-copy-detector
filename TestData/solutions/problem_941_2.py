class Solution:
    def solution_941_2(self, queries: List[int], m: int) -> List[int]:
        l = [i+1 for i in range(m)]
        x = []
        for i in queries:
            n = l.index(i)
            x.append(n)
            l.insert(0,l.pop(n))
        return x