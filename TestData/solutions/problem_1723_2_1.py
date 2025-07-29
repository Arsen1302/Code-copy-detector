class Solution:
    def solution_1723_2_1(self, root: Optional[TreeNode], queries: List[int]) -> List[List[int]]:
        nums = []
        def solution_1723_2_2(node):
            if node:
                nums.append(node.val)
                if node.left:
                    solution_1723_2_2(node.left)
                if node.right:
                    solution_1723_2_2(node.right)
        
        solution_1723_2_2(root)
        nums.sort()
        n = len(nums)
        ans = []
        
        for i in range(len(queries)):
            left = 0
            right = n - 1
            
            while right > left:
                mid = (left + right)//2
                if nums[mid] == queries[i]:
                    left = right = mid
                elif nums[mid] > queries[i]:
                    right = mid
                elif nums[mid] < queries[i]:
                    left = mid + 1
            
            if nums[right] == queries[i]:
                sub = (nums[left], nums[right])
            elif nums[right] > queries[i]:
                sub = (nums[right-1], nums[right]) if right - 1 >= 0 else (-1, nums[right])
            elif nums[right] < queries[i]:
                sub = (nums[left], nums[left]) if left + 1 < n else (nums[left], -1)
            
            ans.append(sub)
        
        return ans