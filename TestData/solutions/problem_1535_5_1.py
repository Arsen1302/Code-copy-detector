class Solution:
    def solution_1535_5_1(self, candies: List[int], k: int) -> int:
        # The lower bound is 1 and higher bound is maximum value from candies. 
        lo, hi = 1, max(candies)
        # This higher bound is not generally possible except for cases like candies = [5,5,5,5] &amp; k = 4
        res = 0 # Current maximum result
        if sum(candies) < k: # If true then we cannot give even 1 candy to each child thus return 0
            return 0
        
        def solution_1535_5_2(pile_size): # Criterion function
            count = 0
            for c in candies:
                count += c // pile_size
            return count >= k
        
        while lo <= hi: # Binary Search Algorithm 
            mid = (lo + hi + 1) // 2 # Expected answer
            if solution_1535_5_2(mid): # Check if mid is a possible answer.
                res = mid # Update the current maximum answer
                lo = mid + 1 # Check ahead of mid
            else:
                hi = mid - 1 # Check below mid
        return res