class Solution:
    def solution_481_4(self, order: str, s: str) -> str:
        
        #output string
        sout = ''
        count = 0
        #iterate though the order
        for sortletter in order:
            #check if sortletter is in s, add to output var
            count = s.count(sortletter)
            if count > 0:
                sout = sout+ sortletter*(count)
                #remove the letter from s
                s = s.replace(sortletter,'',count)
            count = 0
        return(sout+s)