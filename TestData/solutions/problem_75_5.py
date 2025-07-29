class Solution:
    def solution_75_5(self, n: int) -> str:
        ans=''
        while n:
            ans=chr(ord('A')+((n-1)%26))+ans
            n=(n-1)//26
        return ans