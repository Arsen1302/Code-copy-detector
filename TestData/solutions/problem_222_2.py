class Solution:
    def solution_222_2(self, A: List[int]) -> int:
        if len(A) < 3: return 0
        
        res, counter = 0, 2
        last_dif = A[1] - A[0]
        
        for index, num in enumerate(A[2:], 1):
            
            if last_dif == num - A[index]:
                counter += 1  
            else:
                if counter >= 3:
                    res += (counter - 1) * (counter - 2) // 2   
                counter = 2
                last_dif = num - A[index]
                
                
        if counter >= 3:
            res += (counter - 1) * (counter - 2) // 2
        return res