class Solution:
    def solution_282_4(self, area: int) -> List[int]:
        for i in range(int(area**.5),-1,-1):
            if area%i == 0:
                break
        return [area//i,i]