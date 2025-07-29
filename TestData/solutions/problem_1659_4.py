class Solution:
    def solution_1659_4(self, s: str, distance: List[int]) -> bool:
        n = len(s)
        for i in range(n-1):
            for j in range(i+1,n):
                if s[i] == s[j]:
                    if distance[ord(s[i]) - 97]  != (j - i - 1):
                        return False
                    else:
                        break
        return True