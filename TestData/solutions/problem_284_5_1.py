class Solution:
    def solution_284_5_1(self, nums: List[int], target: int) -> int:
        
        # Global memorization to save time
        dic = defaultdict(int)
        l = len(nums)
        
        # DFS Tree with memorization
        def solution_284_5_2(i, tol):
            # End condtion for recursive function
            if i == l:
                return 1 if tol == target else 0
            # Addition step to save time 
            # Get the memorization from previous DFS path
            if (i, tol) in dic:
                return dic[(i, tol)]
            # No memorization calulate path after equal to target recursively
            else:
                dic[(i,tol)] = solution_284_5_2(i+1, tol + nums[i]) + solution_284_5_2(i+1, tol - nums[i])
                return dic[(i,tol)]
        
        return solution_284_5_2(0,0)