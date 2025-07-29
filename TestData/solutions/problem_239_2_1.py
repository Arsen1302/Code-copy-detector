class Solution(object):
    def solution_239_2_1(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: int
        """
        self.targetSum=targetSum
        self.hashmap={0:1}
        self.prefix=0
        self.result=0
        
        self.solution_239_2_2(root)
        
        return self.result
    def solution_239_2_2(self, root):
        
        if root is None:
            return
        
        self.prefix+=root.val
        if self.prefix-self.targetSum in self.hashmap:
            self.result+=self.hashmap[self.prefix-self.targetSum]
        
        if self.prefix in self.hashmap:
            self.hashmap[self.prefix]+=1
        else:
            self.hashmap[self.prefix]=1
            
        self.solution_239_2_2(root.left)
        self.solution_239_2_2(root.right)
        
        self.hashmap[self.prefix]-=1
        self.prefix-=root.val