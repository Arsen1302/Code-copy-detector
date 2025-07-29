class Solution:
    def solution_236_2(self, s: str) -> int:
        
        #create a list based on a space split
        slist = list(s.split(" "))
        
        #return the len of list minus empty item
        return(len(slist)-slist.count(""))