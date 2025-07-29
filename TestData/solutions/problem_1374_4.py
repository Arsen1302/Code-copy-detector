class Solution:
    def solution_1374_4(self, operations: List[str]) -> int:
        x=0
        for i in operations:
            if(i=="X--" or i=="--X"):
                x-=1
            else:
                x+=1
        return x