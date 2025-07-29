class Solution:
    def solution_560_3_1(self, arr: List[int]) -> int:
        
        # NOTE: returning zero if next element in fib seq
        # is not found is the crux of the optimization. If
        # ignored time limit in the test cases exceeds.
        
        # Init
        arr.sort()
        n = len(arr)
        A = set(arr)
        t = defaultdict(lambda: 0)
        
        # A Function to compute fib length
        # starting with a sequence i,j,i+j,...
        def solution_560_3_2(i: int, j: int) -> int:
            
            nonlocal t
           
            # If key is not processed
            if (i,j) not in t:
                
                # Continue if fib seq valid
                k = i + j
                if k not in A:
                    return 0
                else:
                    t[(i,j)] = solution_560_3_2(j, k) + 1
                
            return t[(i,j)]
        
        # For all possible combination
        max_len = -sys.maxsize
        for i in range(0,n-1):
            for j in range(i+1,n):
                max_len = max(max_len, solution_560_3_2(arr[i],arr[j]))
        
        # Add 2 to the max_len if it is not zero, this will include
        # the length of the first two elements which are not counted
        # previously.
        return max_len + 2 if max_len else 0