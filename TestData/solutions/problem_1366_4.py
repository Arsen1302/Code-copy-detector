class Solution:
    def solution_1366_4(self, word: str, ch: str) -> str:
        count=0
        n=len(word)
        for i in range(n):
            if word[i]==ch:
                count=i
                break
        ans1,ans2=word[:count+1],word[count+1:]
        ans=ans1[::-1]
        return ans+ans2