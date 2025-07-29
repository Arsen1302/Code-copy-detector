class Solution:

    def solution_504_4_1(self, s: str) -> List[str]:
        if len(s) == 1:
            return [s]
        ans = [] if s.startswith("0") else [s]
        if s.endswith("0"):
            return ans
        for i in range(1, len(s)):
            a, b = s[:i], s[i:]
            if a.startswith("0") and len(a) > 1:
                break
            ans.append(f"{a}.{b}")
        return ans

    def solution_504_4_2(self, s: str) -> List[str]:
        s = s[1:-1]
        ans = []
        for i in range(1, len(s)):
            a, b = s[:i], s[i:]
            for x, y in product(self.solution_504_4_1(a), self.solution_504_4_1(b)):
                ans.append(f"({x}, {y})")
        return ans