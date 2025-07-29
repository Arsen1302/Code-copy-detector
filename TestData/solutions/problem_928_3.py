class Solution:
    def solution_928_3(self, s: str) -> str:
        table = [0 for _ in range(len(s))]
        longest_prefix = 0
        for j in range(1, len(s)):
            while longest_prefix>0 and s[longest_prefix]!=s[j]:
                longest_prefix = table[longest_prefix-1]
            if s[longest_prefix]==s[j]:
                longest_prefix+=1
                table[j] = longest_prefix
        return s[:table[-1]]