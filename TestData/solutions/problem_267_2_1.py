class Solution:
    def solution_267_2_1(self, matchsticks: List[int]) -> bool:
        # There should be at least 4 matchsticks.
        if len(matchsticks) < 4:
            return False
        
        # Sum of matchstick lengths should be divisble by four.
        side_length, remainder = divmod(sum(matchsticks), 4)
        if remainder != 0:
            return False
        
        # There shouldn't be any single matchstick with length greater than side_length.
        if max(matchsticks) > side_length:
            return False
        
        # Check if partitioning is possible.
        return self.solution_267_2_2(matchsticks, 4, side_length)
    
    def solution_267_2_2(self, nums, k, target):
        buckets = [0] * k
        nums.sort(reverse=True)  # pruning
        
        def solution_267_2_3(idx):
            # If all elements have been used, check if all are equal.
            if idx == len(nums):
                return len(set(buckets)) == 1
            
            # Try placing numbers in each bucket.
            for b in range(k):
                buckets[b] += nums[idx]
                if buckets[b] <= target and solution_267_2_3(idx + 1):
                    return True
                buckets[b] -= nums[idx]
                
                # Pruning: Buckets are filled from left to right. If any bucket remains empty,
                # then all buckets to the right of it will also be empty.
                if buckets[b] == 0:
                    break
            
            return False
        
        return solution_267_2_3(0)