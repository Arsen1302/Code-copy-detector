class Solution:
    
    def solution_480_5_1(self):
        self.table = {(0,0):1, (0,3):1}
        self.mod = 1000000007
    
    def solution_480_5_2(self, pos, state):
        if pos < 0: return 0
        elif (pos, state) not in self.table:
            if state == 0:
                self.table[(pos, state)] = self.solution_480_5_2(pos-1, 3)
            elif state == 1:
                self.table[(pos, state)] = self.solution_480_5_2(pos-1, 0) + self.solution_480_5_2(pos-1, 2)
            elif state == 2:
                self.table[(pos, state)] = self.solution_480_5_2(pos-1, 0) + self.solution_480_5_2(pos-1, 1)
            elif state == 3:
                self.table[(pos, state)] = self.solution_480_5_2(pos-1, 0) + self.solution_480_5_2(pos-1, 1) + self.solution_480_5_2(pos-1, 2) + self.solution_480_5_2(pos-1, 3)
        
        self.table[(pos, state)] %= self.mod
        return self.table[(pos, state)]
    
    def solution_480_5_3(self, n: int) -> int:
        
        return self.solution_480_5_2(n-1, 3)