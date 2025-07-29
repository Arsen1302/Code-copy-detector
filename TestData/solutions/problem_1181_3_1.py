class Solution:
    def solution_1181_3_1(self, lowLimit: int, highLimit: int) -> int:
        box = {}
        for balls in range(lowLimit,highLimit+1):
            boxNo = self.solution_1181_3_2(balls)
            if boxNo in box:
                box[boxNo] += 1
            else:
                box[boxNo] = 1
        
        max = 0
        for key in box:
            if box[key] > max:
                max = box[key]
        return max
        
        
    def solution_1181_3_2(self,n):
        ans = 0 
        while n > 0:
            ans += n % 10 
            n = n // 10
        return ans