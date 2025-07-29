class Solution:
    def solution_914_3(self, light: List[int]) -> int:
        max=0
        c=0
        for i in range(len(light)):
            if(light[i]>max):
                max=light[i]
            if(max==i+1):
                c=c+1
        return c