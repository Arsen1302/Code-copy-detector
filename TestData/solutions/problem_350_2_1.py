class Solution:
    def solution_350_2_1(self, p1, p2, p3, p4) :
        def solution_350_2_2(p1, p2, p3) :
            l = sorted([(p1[0]-p2[0])**2+(p1[1]-p2[1])**2, (p1[0]-p3[0])**2+(p1[1]-p3[1])**2, (p3[0]-p2[0])**2+(p3[1]-p2[1])**2])
            return l[0]+l[1]==l[2] and l[0]==l[1]!=0
        return solution_350_2_2(p1,p2,p3) and solution_350_2_2(p2,p3,p4) and solution_350_2_2(p3,p4,p1)