class Solution:
    def solution_350_1_1(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        def solution_350_1_2(point1,point2):
            return (point1[0]-point2[0])**2+(point1[1]-point2[1])**2
            
        D=[
        solution_350_1_2(p1,p2),
        solution_350_1_2(p1,p3),
        solution_350_1_2(p1,p4),
        solution_350_1_2(p2,p3),
        solution_350_1_2(p2,p4),
        solution_350_1_2(p3,p4)
        ]
        D.sort()
        return 0<D[0]==D[1]==D[2]==D[3] and D[4]==D[5]