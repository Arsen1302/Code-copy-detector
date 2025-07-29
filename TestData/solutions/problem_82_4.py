class Solution:
    def solution_82_4(self, s: str) -> List[str]:
        tmp = set()
        ans = set()
        for i in range(0, len(s)-9):
            string = s[i:i+10]
            if string in tmp:
                ans.add(string)
            else:
                tmp.add(string)
        return ans