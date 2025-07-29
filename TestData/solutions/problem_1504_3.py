class Solution:
    def solution_1504_3(self, time: List[int], totalTrips: int) -> int:
        
        from collections import Counter
        import numpy as np
        
        dic = Counter(time)
        
        k_arr, v_arr = np.array(list(dic.keys())), np.array(list(dic.values()))
        
        idx, res = 1, 0
        
        while 1:
            temp = idx * np.ones_like(k_arr)
            left = np.remainder(temp, k_arr)
            res += sum(v_arr[left == 0])
            if res >= totalTrips: return idx
            idx += 1