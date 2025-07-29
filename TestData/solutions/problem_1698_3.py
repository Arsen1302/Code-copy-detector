class Solution:
    def solution_1698_3(self, event1: List[str], event2: List[str]) -> bool:
        return event1[0] <= event2[0] <= event1[1] or event2[0] <= event1[0] <= event2[1]