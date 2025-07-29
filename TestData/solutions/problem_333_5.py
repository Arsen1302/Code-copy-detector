class Solution(object):
    def solution_333_5(self, nums: List[int], k: int) -> int:
        count = 0
        
        hashmap = {0: 1}
        curr_cumulative_sum = 0
        
        for num in nums:
            curr_cumulative_sum += num
            
            if curr_cumulative_sum - k in hashmap:
                count += hashmap[total - k]
                
            try:
                hashmap[curr_cumulative_sum] += 1
            except KeyError:
                hashmap[curr_cumulative_sum] = 1
                
        return count