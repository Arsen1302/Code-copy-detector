class Solution:
    def solution_1150_5(self, customers: List[List[int]]) -> float:
        totalTime = 0
        current = 0
        for arr, time in customers:
            current = max(current, arr) + time
            totalTime += current - arr
        return totalTime/len(customers)