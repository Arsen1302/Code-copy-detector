class Solution:
    def solution_1048_4(self, n: int) -> int:
        
        
        q = [(n,0)]
        
        seen = set()
        while q:
            
            data = q.pop(0)
            left, days = data[0],data[1]
            if left == 0:
                return days 
            
            if (left) in seen:
                continue
            
            seen.add((left))
            
            
            q.append((left-1, days+1))
            
            one = left % 2 == 0
            
            if one:
                q.append((left//2 , days +1))
            
            two = left % 3 == 0
            
            if two:
                q.append(((left//3), days+1))
        ```