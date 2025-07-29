class Solution:
    def solution_714_1_1(self, nums1: List[int], nums2: List[int]) -> int:
        e1=len(nums1)
        e2=len(nums2)
        @lru_cache(None,None)
        def solution_714_1_2(s1,s2):
            best=-float('inf')
            if s1>=e1 or s2>=e2:
                return 0
            temp=[]
            op1=0
			#finding element in array2 which is equal to element in array1 from where we want to draw line
            for idx in range(s2,e2):
                if nums2[idx]==nums1[s1]:
                    temp.append(idx)
			#drawing line to all those element and checking which gives maximum value
            for j in temp:
                op1=1+solution_714_1_2(s1+1,j+1)
                best=max(op1,best)
			#choosing to not draw line from current element of array1
            op2=solution_714_1_2(s1+1,s2)
			#returning max of both options.
            return max(op2,best)
        return solution_714_1_2(0,0)