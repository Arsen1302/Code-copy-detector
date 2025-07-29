class Solution:
    def solution_1236_2(self, logs: List[List[int]], k: int) -> List[int]:
        # use two-layer dict 
        # first layer record user; second layer record the active minutes 
        
        # 1. Put info. in 2-layer dict O(n)
        d = {}
        for (user, active_min) in logs:
            if not (user in d):
                d[user] = {}
                
            user_log = d[user]
            user_log[active_min] = True 
            
        # 2. Extract info. from 2-layer dict (at most O(n))
        result = [0] * k 
        for user in d:
            result[len(d[user])-1] += 1 # len(d[user]) must >= 1 to exist 
            
        return result