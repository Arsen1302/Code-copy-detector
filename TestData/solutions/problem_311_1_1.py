class Solution:
    def solution_311_1_1(self, n: int) -> int:
        self.count = 0
        self.solution_311_1_2(n, 1, [])
        return self.count
        
    def solution_311_1_2(self, N, idx, temp):
        if len(temp) == N:
            self.count += 1
            return
        
        for i in range(1, N+1):
            if i not in temp and (i % idx == 0 or idx % i == 0):
                temp.append(i)
                self.solution_311_1_2(N, idx+1, temp)
                temp.pop()