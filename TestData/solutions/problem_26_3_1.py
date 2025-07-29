class Solution:
    def solution_26_3_1(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        self.targetSum, self.ans = targetSum, []            # variable initialization
        self.solution_26_3_2(root, 0, [])                      # calling function get path sum
        return self.ans                                     # return answer
        
    def solution_26_3_2(self, root, psum, path):
        if not root: return None                            # if not root return None
        if not root.left and not root.right:                # if curr node is leaf
            if root.val + psum == self.targetSum:           # if path sum from root to leaf = target sum
                path.append(root.val)                       # append node value to path
                self.ans.append([e for e in path])          # add path to ans list
                path.pop(-1)                                # remove node value from path
                return;                                     # return
        path.append(root.val)                               # append node value to path
        self.solution_26_3_2(root.left, psum + root.val, path) # left traversal
        self.solution_26_3_2(root.right, psum + root.val, path)# right traversal
        path.pop(-1)                                        # remove node value from path