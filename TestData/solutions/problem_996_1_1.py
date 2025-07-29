class Solution:
    def solution_996_1_1(self,arr, d, m, k) -> bool:
        '''
        d -> days
        m -> bouquets
        k -> adjacent flowers
        
        return bool
        '''
        arr = [10**9] + arr + [10**9] #appending array with maximum values
        idx = []
        for i in range(len(arr)):
            if arr[i] > d:
                idx.append(i)
        cnt = 0
        for i in range(len(idx)-1):
            # how many bouquet can we make out of an interval of valid flowers 
            cnt += (idx[i+1] - idx[i] - 1) // k
        
        # return if count >= m
        return cnt >= m

    def solution_996_1_2(self, arr: List[int], m: int, k: int) -> int:
        if m*k > len(arr):
            return -1
        lo, hi = 1, max(arr)
        
        while(hi >= lo):
            mid = (hi+lo)//2
            if(self.solution_996_1_1(arr, mid, m, k) == True):
                hi = mid
            else:
                lo = mid+1
            if(hi == lo): break
    
        if self.solution_996_1_1(arr, lo, m, k):
            return lo
        else:
            return hi