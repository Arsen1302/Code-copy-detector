class Solution:
    def solution_787_1(self, arr: List[int]) -> int:
        n = len(arr)
        #maximum subarray starting from the last element i.e. backwards 
        prefix_sum_ending = [float('-inf')]*n
        #maximum subarray starting from the first element i.e forwards
        prefix_sum_starting = [float('-inf')]*n
        prefix_sum_ending[n-1] = arr[n-1]
        prefix_sum_starting[0] = arr[0]
        
        for i in range(1,n):
            prefix_sum_starting[i] = max(prefix_sum_starting[i-1]+arr[i], arr[i])
        for i in range(n-2,-1,-1):
            prefix_sum_ending[i] = max(prefix_sum_ending[i+1]+arr[i], arr[i])
           
        max_without_deletion = max(prefix_sum_starting)
        max_with_deletion = float('-inf')
        for i in range(1,n-1):
            max_with_deletion = max(max_with_deletion, prefix_sum_starting[i-1]+prefix_sum_ending[i+1])
            
        return max(max_without_deletion, max_with_deletion)