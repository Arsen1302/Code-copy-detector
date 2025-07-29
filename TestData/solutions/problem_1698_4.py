class Solution:
    def solution_1698_4(self, event1: List[str], event2: List[str]) -> bool:
        start1 = int(event1[0][:2]) * 60 + int(event1[0][3:])
        end1 = int(event1[1][:2]) * 60 + int(event1[1][3:])
        start2 = int(event2[0][:2]) * 60 + int(event2[0][3:])
        end2 = int(event2[1][:2]) * 60 + int(event2[1][3:])
        return True if start1 <= start2 <= end1 or start2 <= start1 <= end2 else False