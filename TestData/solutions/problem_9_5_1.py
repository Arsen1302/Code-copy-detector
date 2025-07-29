class Solution:
    def solution_9_5_1(self):
        self.revNum = 0
    def solution_9_5_2(self, x: int) -> bool:
        if x < 0: return False
        def solution_9_5_3(num): # num = 54321
            if num == 0: # False
                return self.revNum
            lastVal = num%10 # 54321 --> 1
            self.revNum = self.revNum*10+lastVal
            return(solution_9_5_3(num//10))
        return x == solution_9_5_3(x)