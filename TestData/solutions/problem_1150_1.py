class Solution:
    def solution_1150_1(self, customers: List[List[int]]) -> float:
        arr = []
        
        time = 0
        
        for i , j in customers:
            if(i > time):
                time = i + j
            else:
                time += j
            arr.append(time - i)
        
        return sum(arr) / len(arr)