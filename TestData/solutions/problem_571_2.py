class Solution:
    def solution_571_2(self, A: str, B: str) -> List[str]:
        A = A.split() + B.split() # Simply add both the strings by converting it into list using split()
        resLis = [] # to store the result list
        for i in A: #traverse the list 
            if A.count(i) == 1: #if the count of string present in list is 1 then append it to the resLis
                resLis.append(i)
        return resLis #return the resLis