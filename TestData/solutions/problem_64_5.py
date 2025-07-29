class Solution:
    def solution_64_5(self, s: str) -> str:
        s=list(s.split())  #split at spaces and convert to list
        s=s[::-1]  #reverse the list
        return (" ".join(s))  #join the list with spaces