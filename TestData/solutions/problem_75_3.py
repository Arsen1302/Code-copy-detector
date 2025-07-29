class Solution:
    def solution_75_3(self, columnNumber: int) -> str:
        ans = ""
        
        while columnNumber:
            columnNumber -= 1
            ans = chr(65 + columnNumber % 26) + ans
            columnNumber //= 26
        
        return ans
	```