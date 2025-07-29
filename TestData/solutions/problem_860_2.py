class Solution:
    def solution_860_2(self, s: str) -> str:
        
        fn = lambda i: chr(96+int(i)) #convert number to char
        
        ans = []
        i = len(s)-1
        while i >= 0:
            if s[i] == "#": 
                ans.append(fn(s[i-2:i]))
                i -= 3
            else: 
                ans.append(fn(s[i]))
                i -= 1
        
        return "".join(reversed(ans))