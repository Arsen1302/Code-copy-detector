class Solution:
    def solution_103_5_1(self, k: int, n: int) -> List[List[int]]:
        
        answer = []
        path = []
        
        def solution_103_5_2(idx, total):
            if len(path) > k:
                return
            if total > n:
                return
            if total == n and len(path) == k:
                answer.append(path.copy())
                return 
                
            for i in range(idx, 10):
                path.append(i)
                solution_103_5_2(i+1, total + i)
                path.pop()
        
        solution_103_5_2(1, 0)
        return  answer