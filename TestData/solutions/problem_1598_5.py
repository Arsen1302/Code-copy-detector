class Solution:
    def solution_1598_5(self, s: str) -> int:
        tempCount = 0
        count=0 
        for i in s : 
            if i =="|":
                tempCount+=1
            if tempCount==2:
                tempCount = 0 
            if tempCount==0 and i =="*":
                count+=1
        return(count)