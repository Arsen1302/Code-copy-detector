class Solution:
    def solution_1628_3(self, g: List[int]) -> int:
        n = len(g)
        
        g.sort()
        
        curr_group = 1
        curr_group_sum = 0
        idx = 0
        count = 0
        
        while idx < n:
			# We don't have enough elements to put in the next group, let's put them in the current group and return.
            if n - idx < curr_group:
                return count
            
			# Calculate the next group sum.
            next_group_sum = 0   
            c = 0
            while c < curr_group:
                next_group_sum += g[idx]
                idx += 1
                c += 1
                
			# If the next group sum is not enough, put the remaining elements in the current group and return early.
			if next_group_sum <= curr_group_sum:
                return count 
				
			count += 1
			curr_group_sum = next_group_sum
			curr_group += 1

        return count