class Solution:
    def solution_1190_4(self, a: int, b: int, c: int) -> int:
        a, b, c = sorted([a, b, c], reverse=True)
        sub = math.ceil((a + b - c) / 2)
        return b + min(a-b, c) if sub > b else sub + (a-sub) + (b-sub)