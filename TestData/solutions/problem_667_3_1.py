class Solution:
    
    def solution_667_3_1(self):
        self.order = collections.defaultdict(dict)
    
    def solution_667_3_2(self, node, x, y):
        if not node:
            return
        self.order[x][y] = self.order[x].get(y, []) + [node.val]
        self.solution_667_3_2(node.left, x-1, y-1)
        self.solution_667_3_2(node.right, x+1, y-1)
    
    def solution_667_3_3(self, root: TreeNode) -> List[List[int]]:
        # placeholder to store the list of reports
        verticalOrder = []
        
        # step 1 : traverse the tree, to create list of values at each (x, y)
        self.solution_667_3_2(root, 0, 0)
        
        # step 2 : at each x, sort the values first by y, then by value
        for x in sorted(self.order):
            report = []
            for y in sorted(self.order[x], reverse=True):
                report += sorted(self.order[x][y]) 
            verticalOrder.append(report)
        
        # step 3 : return the list of reports
        return verticalOrder