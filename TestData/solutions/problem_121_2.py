class Solution:
    def solution_121_2(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # if in the current recursion level
        # you find either p or q, return that node
        # if you instead find a None, return None
        # since we're handling both the cases below
        if root is None or root == p or root == q:
            return root
        
        # find either p or q in the left subtree
        # we're expecting this to return one of
        # [None, p, q] and for both the left and right
        # subtree
        l = self.solution_121_2(root.left, p, q)
        r = self.solution_121_2(root.right, p , q)
        
        # since values in the tree are unique
        # and this root's left and right subtree
        # has either p and q each, this is the root
        # we're looking for. We're not worried about
        # what values are returned, it's more like
        # we have presence of either p or q in both
        # subtrees, so this has to be our result
        if l and r:
            return root
        
        # if either of the node doesn't contain
        # p or q, just return either None or the
        # one node which has either p or q
        return l if l else r