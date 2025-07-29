class Solution(object):
    def solution_545_4_1(self,a,b):
            if a == 0:
                return b
            return self.solution_545_4_1(b % a, a)
    def solution_545_4_2(self,a,b):
        return (a / self.solution_545_4_1(a,b))* b
    def solution_545_4_3(self, p,q):
        
        solution_545_4_2=self.solution_545_4_2(p,q)
        m=solution_545_4_2//p
        n=solution_545_4_2//q
        if n%2==0:
            return 2
        if m%2==0:
            return 0
        return 1
    
    
# basically you can just ignore the north wall and imagine the mirrors 
# as two parallel mirrors with just extending east and west walls and the end points of east walls are made of 0 reflector then 1 reflector the oth the 1th and so onn....
# eventually we gotta find the point where m*p=n*q
# and we can find m and n by solution_545_4_2 of p and q 
# now the consept is simple .....
# if number of extensions of q(ie n) is even that means the end reflection must have happened on west wall ie. reflector 2 else 
# else there are two possibility reflector 1 or 0 which depends on the value of m(ie. the full fledged square extentions) if its even or odd