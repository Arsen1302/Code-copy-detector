class Solution:
    def solution_1031_5_1(self):
        self.ans=0
    def solution_1031_5_2(self, root: TreeNode, distance: int) -> int:
        self.solution_1031_5_3(root,distance)
        return self.ans
    def solution_1031_5_3(self,root,distance):
        if not root:
            return []
        if not root.left and not root.right:
            return [1]
        leftNodes=self.solution_1031_5_3(root.left,distance)
        rightNodes=self.solution_1031_5_3(root.right,distance)
        for ln in leftNodes:
            for rn in rightNodes:
                if ln+rn<=distance:
                    self.ans+=1
        leftNodes=list(map(lambda x:x+1,leftNodes))
        rightNodes=list(map(lambda x:x+1,rightNodes))
        return leftNodes+rightNodes