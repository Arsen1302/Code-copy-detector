class Solution:
    def solution_1144_3_1(self, cuboids: List[List[int]]) -> int:
        def solution_1144_3_2(base, box):
            if base[0] >= box[0] and base[1] >= box[1] and base[2] >= box[2]:
                return True
            else:
                return False

        [i.sort() for i in cuboids]
        
        cuboids.sort()

        n = len(cuboids)
        curr = [0 for i in range(n+1)]
        nex = [0 for i in range(n+1)]
        for index in range(n-1,-1,-1):
            for parent in range(index - 1,-2,-1):
                take = 0
                if  parent == -1 or solution_1144_3_2(cuboids[index],cuboids[parent]):
                    take = cuboids[index][2] + nex[index+1]
                
                dont = nex[parent+1]
                
                curr[parent+1] = max(take,dont)
            
            nex = curr     
        return nex[0]