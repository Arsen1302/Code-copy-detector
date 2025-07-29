class Solution:
    def solution_1698_2(self, event1: List[str], event2: List[str]) -> bool:
        e1s=int(event1[0][:2])*60 + int(event1[0][3:])
        e1e=int(event1[1][:2])*60 + int(event1[1][3:])
        e2s=int(event2[0][:2])*60 + int(event2[0][3:])
        e2e=int(event2[1][:2])*60 + int(event2[1][3:])
        if e1s<=e2s<=e1e: return True
        if e2s<=e1s<=e2e: return True
        if e1s<=e2e<=e1e: return True
        if e2s<=e1e<=e2e: return True
        else: return False