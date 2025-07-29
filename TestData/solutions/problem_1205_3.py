class Solution:
    def solution_1205_3(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        return sum(item_list[{"type": 0, "color": 1, "name": 2}[ruleKey]] == ruleValue for item_list in items)