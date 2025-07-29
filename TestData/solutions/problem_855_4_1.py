class Solution(object):
    def solution_855_4_1(self, root):
        levels = {}
        
        def solution_855_4_2(curr,prevVal,level):
            if curr==None:
                return
            level+=1
            if level in levels:
                levels[level]+=curr.val
            else:
                levels[level]=curr.val
                
            solution_855_4_2(curr.left,curr.val,level)
            solution_855_4_2(curr.right,curr.val,level)
            
        solution_855_4_2(root,0,0)
        return levels[max(levels)]