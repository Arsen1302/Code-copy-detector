class Solution:
    def solution_725_4(self, s: str) -> str:
        ans = []
        i = 0
        for i in s:
            if len(ans) > 0:
                if i == ans[-1]:
                    ans.pop()
                else:
                    ans.append(i)
            else:
                ans.append(i)
        return ''.join(ans)