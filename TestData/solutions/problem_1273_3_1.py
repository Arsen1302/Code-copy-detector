class Solution:
    def solution_1273_3_1(self, dist: List[int], hour: float) -> int:
        sum_ = sum(dist)
        self.ans = float("inf")
        
        def solution_1273_3_2(speed):
            time = sum([math.ceil(dist[i]/speed) for i in range(len(dist)-1)])
            return (time+(dist[-1]/speed)) <= hour
            
            
        def solution_1273_3_3(left,right):
            while left<=right:
                speed = left + (right-left)//2
                if solution_1273_3_2(speed):
                    self.ans = min(self.ans,speed)
                    right = speed - 1
                else:
                    left = speed + 1
            
        solution_1273_3_3(1,10**7)
        return -1 if self.ans == float("inf") else self.ans