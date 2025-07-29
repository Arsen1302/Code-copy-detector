class Solution:
    def solution_1504_2(self, time: List[int], totalTrips: int) -> int:
        
        from collections import Counter
        import numpy as np
        
        dic = Counter(time)
        k_arr, v_arr = np.array(list(dic.keys())), np.array(list(dic.values()))
        
		# deal with edge cases, eg. time = [1, 1, 1, 1, 1], totalTrip = 5
        if np.size(k_arr) == 1 and k_arr[0] == 1: 
            if totalTrips % v_arr[0] == 0: return totalTrips // v_arr[0]
            else: return totalTrips // v_arr[0] + 1
        
		# binary search
        l, r = min(k_arr), min(k_arr) * totalTrips
        idx = (l + r) // 2   # mid
        
        while l + 1 < r:
            temp = np.sum((idx * np.ones_like(k_arr) // k_arr) * v_arr)
            if temp >= totalTrips:
                r = idx
                idx = (r + l) // 2
            else:
                l = idx
                idx = (r + l) // 2
            
        return r