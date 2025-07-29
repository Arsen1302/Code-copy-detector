class Solution:
    def solution_666_1(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        
        idx_a, idx_b = 0, 0
        size_a, size_b = len(A), len(B)
        
        intersection = []
        
        # Scan each possible interval pair
        while idx_a < size_a and idx_b < size_b :
            
            # Get start-time as well as end-time
            start_a, end_a = A[idx_a]
            start_b, end_b = B[idx_b]
            
            
            # Compute common start time and end time for current interval pair
            common_start = max( start_a, start_b )
            common_end = min( end_a, end_b )
            
            if common_start <= common_end:
                # Find one common overlapped interval
                intersection.append( [common_start, common_end] )
                
            if end_a <= end_b:
                # Try next interval of A
                idx_a += 1
                
            else:
                # Try next interval of B
                idx_b += 1
        
        return intersection