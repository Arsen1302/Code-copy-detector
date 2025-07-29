class Solution:
    def solution_27_5(self, root):
        if not root: #1
            return
        
        if root.left: #2
            self.solution_27_5(root.left) #3
            temp = root.right #4
            root.right = root.left #5
            root.left = None #6
            curr = root.right #7
            
            while curr.right: #8
                curr = curr.right #9
            
            curr.right = temp #10
        
        if root.right: #11
            self.solution_27_5(root.right)