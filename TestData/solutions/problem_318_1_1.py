class Solution:
    def solution_318_1_1(self, timePoints: List[str]) -> int:
        M = 1440
        times = [False] * M
        for time in timePoints:
            solution_318_1_2 = self.solution_318_1_2(time)
            if times[solution_318_1_2]:
                return 0
            times[solution_318_1_2] = True
        
        minutes = [i for i in range(M) if times[i]]
        return min((minutes[i] - minutes[i-1]) % M for i in range(len(minutes)))
        
    def solution_318_1_2(self, time: str) -> int:
        h, m = map(int, time.split(':'))
        return 60*h + m