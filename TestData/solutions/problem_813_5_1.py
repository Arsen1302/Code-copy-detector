class Solution:
    def solution_813_5_1(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        n = len(profit)
        jobs = [(startTime[i],endTime[i],profit[i]) for i in range(n)]
        jobs.sort(key = lambda x: x[1])
        
        def solution_813_5_2(x,low,high):
            
            while low <= high:
                mid = (low + high) // 2
                if jobs[mid][1] <= x : low = mid + 1
                else: high = mid - 1
            
            return high
        
        total_profit = [0]*n
        for index in range(n):
            
            i = solution_813_5_2(jobs[index][0] , 0 , index - 1)
            to_add = total_profit[i] if i != -1 else 0
            total_profit[index] = max(total_profit[index-1],jobs[index][2] + to_add)

        return total_profit[-1]