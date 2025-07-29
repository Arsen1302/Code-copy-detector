class Solution:
    def solution_1641_3(self, pattern: str) -> str:
        ans = []
        dec_count = 0
        for i in range(len(pattern)):
            if pattern[i] == "I":
                for j in range(i, i-dec_count-1,-1):
                    ans.append(str(j+1))
                dec_count = 0
            elif pattern[i] == "D":
                dec_count += 1
                
        # for the remaining dec_count if there is any
        for j in range(len(pattern), len(pattern)-dec_count-1,-1):
            ans.append(str(j+1))
        return "".join(ans)