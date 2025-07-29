class Solution:
    def solution_912_3_1(self, root: Optional[TreeNode]) -> int:
        self.val = 0
        self.solution_912_3_2(root).summ
        return self.val
        
    def solution_912_3_2(self, root):
        if not root:
            return NodeValue(-math.inf, math.inf, 0)
            
        l = self.solution_912_3_2(root.left)
        r = self.solution_912_3_2(root.right)
        
        if l.maxNode < root.val and r.minNode > root.val:
            self.val = max(self.val, root.val + l.summ + r.summ)
            return NodeValue(max(r.maxNode, root.val), min(l.minNode, root.val), root.val + l.summ + r.summ)
        
        return NodeValue(math.inf, -math.inf, 0)
        
class NodeValue:
    def solution_912_3_3(self, maxNode, minNode, summ):
        self.maxNode = maxNode
        self.minNode = minNode
        self.summ = summ