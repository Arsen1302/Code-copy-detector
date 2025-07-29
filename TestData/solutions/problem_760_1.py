class Solution:
    def solution_760_1(self, dominoes: List[List[int]]) -> int:
        m = collections.defaultdict(int)
        ans = 0
        for a, b in dominoes:
            if a > b: a, b = b, a
            v = 10*a + b
            if v in m:
                ans += m[v]
            m[v] += 1
        return ans