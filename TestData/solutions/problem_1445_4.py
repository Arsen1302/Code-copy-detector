class Solution:
    def solution_1445_4(self, s: str, spaces: List[int]) -> str:
        ans = []
        for i in reversed(range(len(s))): 
            ans.append(s[i])
            if spaces and spaces[-1] == i: 
                ans.append(' ')
                spaces.pop()
        return "".join(reversed(ans))