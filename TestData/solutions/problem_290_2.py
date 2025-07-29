class Solution:
    def solution_290_2(self, root: Optional[TreeNode]) -> List[int]:
        if root.val == 0: return [0]
        nums, stack = {}, []
        
        while True:
            while root:
                if root.val in nums.keys(): nums[root.val] += 1
                else: nums[root.val] = 1
                    
                stack.append(root)
                root = root.left
            
            if not stack: break 
            root = stack.pop().right
        
        maxValue = max(nums.values())
        
        return [k for k, v in nums.items() if maxValue == v]