class Solution:
    def solution_714_4_1(self, nums1: List[int], nums2: List[int]) -> int:
        #top-down
        """
        @cache
        def solution_714_4_2(l1=0,l2=0):
            #if no numbers left on any then no possible moves
            if l1 == len(nums1) or l2 == len(nums2):
                return 0
            #see example 1 image
            if nums1[l1] == nums2[l2]:
                return 1+solution_714_4_2(l1+1,l2+1)
            #select which one to skip
            return max(solution_714_4_2(l1+1,l2),solution_714_4_2(l1,l2+1))
        
        return solution_714_4_2()
        """
    
        #bottom-up (blindly converted from top down)
        m,n = len(nums1),len(nums2)
        solution_714_4_2 = [[0]*(n+1) for _ in range(m+1)]

        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                if nums1[i] == nums2[j]:           
                    solution_714_4_2[i][j] = 1+solution_714_4_2[i+1][j+1]
                else:
                    solution_714_4_2[i][j] = max(solution_714_4_2[i+1][j], solution_714_4_2[i][j+1])

        return solution_714_4_2[0][0]