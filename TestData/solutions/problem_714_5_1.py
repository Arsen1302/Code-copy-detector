class Solution: 
    def solution_714_5_1(self,idx1,idx2):
        if idx1 == self.n1 or idx2 == self.n2: 
            return 0
        
        if (idx1,idx2) in self.dp: return self.dp[(idx1,idx2)]
        
        if self.nums1[idx1] == self.nums2[idx2]:
            best = self.solution_714_5_1(idx1+1,idx2+1) + 1
        
        else:
            a = self.solution_714_5_1(idx1+1,idx2)
            b = self.solution_714_5_1(idx1,idx2+1)
            best = a if a > b else b
        
        self.dp[(idx1,idx2)] = best
        
        return best
    
    def solution_714_5_2(self, nums1: List[int], nums2: List[int]) -> int:
        self.n1 = len(nums1)
        self.n2 = len(nums2)
        self.nums1 = nums1
        self.nums2 = nums2
        self.dp = {}
        return self.solution_714_5_1(0,0)