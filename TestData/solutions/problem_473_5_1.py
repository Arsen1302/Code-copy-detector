class Solution:
    def solution_473_5_1(self) :
        self.data = list()
        
    def solution_473_5_2(self, root) :
        if root :
            heappush(self.data, root.val)
            self.solution_473_5_2(root.left)
            self.solution_473_5_2(root.right)
                
    def solution_473_5_3(self, root: Optional[TreeNode]) -> int:
        
        self.solution_473_5_2(root)
        
        tmp = None
        min_num = 10**5+1
        
        while self.data :
            if tmp is not None :
                sec_tmp = heappop(self.data)
                if abs(sec_tmp-tmp) < min_num : min_num = abs(sec_tmp-tmp)
                tmp = sec_tmp
            else :
                tmp = heappop(self.data)
                
        return min_num