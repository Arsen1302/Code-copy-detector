class Solution:
    def solution_919_4_1(self):
        self.arr = []
    def solution_919_4_2(self,root):
        if root is None:
            return []
        else:
            self.solution_919_4_2(root.left)
            self.arr.append(root.val)
            self.solution_919_4_2(root.right)
        return self.arr
    
    def solution_919_4_3(self,left,right,nums):
        if left > right:
            return None
        else:
            mid = (left + right)//2
            root = TreeNode(nums[mid])
            root.left = self.solution_919_4_3(left,mid-1,nums)
            root.right = self.solution_919_4_3(mid+1,right,nums)
        return root
    def solution_919_4_4(self, root: TreeNode) -> TreeNode:
        nums = self.solution_919_4_2(root)
        return self.solution_919_4_3(0,len(nums)-1,nums)