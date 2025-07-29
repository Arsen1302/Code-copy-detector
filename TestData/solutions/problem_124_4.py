class Solution:
    
    def solution_124_4(self, nums: List[int], k: int) -> List[int]:
       
        # Init
        q = [] # This is queue of indexes not num queue of values
        n = len(nums)
        output = []
        
        # Base Case: If window size is 1
        if k == 1:
            return nums
        
        # Base Case: If window size is greater or equal to n
        if n <= k:
            return [max(nums)]
        
        # Fill the first k elements
        for i in range(k):
            
            # Pop till q is a monotonicall decreasing seq
            while q and nums[q[-1]] < nums[i]:
                q.pop()
            
            # Add the current index
            q.append(i)
        
        # First max value for window of size k
        output.append(nums[q[0]])
        
        # Fill elements with index starting from k
        for i in range(k, n):
           
            # Remove out of window elements
            window_start_index = (i-k) + 1
            while q and q[0] < window_start_index:
                q.pop(0)
            
            # Pop till q is a monotonicall decreasing seq
            while q and nums[q[-1]] < nums[i]:
                q.pop()
                
            # Add the current index
            q.append(i)
            
            # queue is not empty then append the current max
            if q:
                output.append(nums[q[0]])
                
        return output