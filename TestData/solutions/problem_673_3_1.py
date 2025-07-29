class Solution:
    def solution_673_3_1(self, root, x, y):
        self.x, self.y = x, y
        self.foundLevel, self.foundParent = None, None            
        return self.solution_673_3_2(root, 0, None)

    def solution_673_3_2(self, node, level, parent):
        if node.val == self.x or node.val == self.y:
            if self.foundLevel and self.foundParent:
				return level == self.foundLevel and parent != self.foundParent
            else:
				self.foundLevel = level; self.foundParent = parent
			
        left =  self.solution_673_3_2(node.left,  level+1, node.val) if node.left  else False
        right = self.solution_673_3_2(node.right, level+1, node.val) if node.right else False

        return left or right