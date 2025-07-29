class Solution:
    def solution_282_3(self, area: int) -> List[int]:
        l = area
        b = 1
        while l > b:
            z = -1
            for i in range(2,int(area**.5)+1):
                if l%i == 0:
                    z = i
            if z == -1 or l//z < b*z:
                break
            else:
                l //= z
                b *= z
        return [l,b]