class Solution:
    def solution_290_5_1(self, root: Optional[TreeNode]) -> List[int]:
        numCount = {}
        self.solution_290_5_2(root,numCount)
        maxCount = max(numCount.values())
        return [k for k,v in numCount.items() if v == maxCount]
    def solution_290_5_2(self,root,numCount):
        if root is None:
            return
        if root.val not in numCount:
            numCount[root.val] = 1
        else:
            numCount[root.val] += 1
        self.solution_290_5_2(root.left,numCount)
        self.solution_290_5_2(root.right,numCount)