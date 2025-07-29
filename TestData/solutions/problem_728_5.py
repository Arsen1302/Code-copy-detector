class Solution:
    def solution_728_5(self, heights: List[int]) -> int:
        #determine max height in list
        maxHeight = max(heights)
        #make a bucket list with maxHeight + 1 as range
        bucket = [0 for x in range(maxHeight + 1)]
        #fill the bucket
        for n in heights:
            bucket[n] += 1
        
        i = 0
        counter = 0
        #iterate through heights 
        for n in heights:
            #make sure we're always on a non-zero element in the bucket
            while bucket[i] == 0: i += 1
            #if bucket index is not equal to element value of heights,
            #then increment counter
            if i != n: counter += 1
            #decrement the count in the bucket on every iteration
            bucket[i] -= 1
        
        return counter