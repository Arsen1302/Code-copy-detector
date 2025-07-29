class Solution:
    def solution_1205_2(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        return sum(1 for t, c, n in items if (ruleKey, ruleValue) in (("type", t), ("color", c), ("name", n)))