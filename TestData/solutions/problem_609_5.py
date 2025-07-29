class Solution:
    def solution_609_5(self, arr: List[int]) -> List[int]:
        indices = deque([])
        N = len(arr)
        ans = [-1,-1]
        
        ## collect all indices of 1
        for idx, val in enumerate(arr):
            if val: 
                indices.append(idx)
                
        if not indices:
            return [0, N-1]
        
        if len(indices) %3 != 0: 
            return [-1, -1]
    
        start = 0
        end = len(indices)-1
        
        s = indices[start]
        
        # if ending in zero, the right most part of 3 parts, should always be from end of middle chunk-until end of array
        endsInZero = (arr[-1] == 0)
        
        # s....index[start]...index[end]....#
        # chunk1 - starts with the first 1
        # chunk2 - start with chunk1 end + 1 or 1st one after chunk1 
        # chunk3 - start with chunk2+1 until end 
        
        ## if the array ends in zero, then the calcuation should be from chunk1+len(last_chunk), chunk2+len(last_chunk) and its edge cases.  
        
        while start < end:
            if endsInZero:
                edge_len = N-1-indices[end]
                medge_index = min(indices[end], indices[start+1]+edge_len+1)
                ## Edge case, if between middle index edge and end if there are 1s
                medge_index = max(medge_index, indices[end-1])
                
                ## check if the lengths are equal, chunk1 and chunk3 have edge_len, hence only compare with middle.
                if medge_index - indices[start+1] == edge_len+1:
                    if arr[s:s+edge_len+1] == arr[indices[end]:]  == arr[indices[start+1]: medge_index]:
                        return (s+edge_len,medge_index)
            else:
                ## check if the lengths are equal
                if indices[start]-s ==  N-indices[end]-1 == indices[end-1]-indices[start+1]:
                    if arr[s:indices[start]+1] == arr[indices[end]:] == arr[indices[start+1]:indices[end-1]+1]:
                        return (indices[start],indices[end-1]+1)
                
            start += 1
            end -= 1
                    
        return ans