class Solution:
    def solution_702_4_1(self, root: Optional[TreeNode]) -> int:
        
        # defining a global variable for recursive solution_702_4_2 to modify
        ret = [0]
        def solution_702_4_2(curr, currpath):
            if curr is None:
                return
            
            # case where leaf node has been reached
            if curr.left is None and curr.right is None:
                currpath.append(curr.val)
                bin_str = "".join(map(str, currpath))
                ret[0] += int(bin_str, 2)
                currpath.pop()
                return
            
            # append the current node's value to the array before processing children
            currpath.append(curr.val)
            solution_702_4_2(curr.left, currpath)
            solution_702_4_2(curr.right, currpath)
            
            # remove the current node's value before returning to callee
            currpath.pop()
            
        solution_702_4_2(root, [])
        return ret[0]