class Solution:
    def solution_1027_2(self, s: str) -> int:
        ans = 0
        leftSet, leftCount = set(), []
        for idx, ch in enumerate(s):
            leftSet.add(ch)
            leftCount.append(len(leftSet))
        
        rightSet = set()
        for idx in range(len(s)-1, 0, -1):
            rightSet.add(s[idx])
            if len(rightSet) == leftCount[idx-1]:
                ans += 1
        return ans