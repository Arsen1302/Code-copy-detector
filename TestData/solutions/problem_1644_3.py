class Solution:
    def solution_1644_3(self, s: str) -> int:
        c=0
        for i in range(len(s)):
            if "01" in s:
                s=s.replace("01","10")
                c+=1
        return(c)
		```