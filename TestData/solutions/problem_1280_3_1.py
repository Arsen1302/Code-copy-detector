class Solution:
    def solution_1280_3_1(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        a, b, c = [],[],[]
        a_,b_,c_="","",""
        base = ord("a")
        
        def solution_1280_3_2(l,s):
            for i in s:
                l.append(ord(i)-base)
            return l
        
        def solution_1280_3_3(x,l):
            for i in l:
                x += str(i)
            return x
        
        a = solution_1280_3_2(a,firstWord)
        b = solution_1280_3_2(b,secondWord)
        c = solution_1280_3_2(c,targetWord)
        
        a_ = solution_1280_3_3(a_,a)
        b_ = solution_1280_3_3(b_,b)
        c_ = solution_1280_3_3(c_,c)
        
        return(( int(a_)+int(b_)) == int(c_))