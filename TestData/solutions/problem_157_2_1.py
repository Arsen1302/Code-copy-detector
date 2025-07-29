class Solution:
    def solution_157_2_1(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        
        def solution_157_2_2(arr, k):
            """Return largest sub-sequence of arr of size k."""
            ans = []
            for i, x in enumerate(arr): 
                while ans and ans[-1] < x and len(ans) + len(arr) - i > k: ans.pop()
                if len(ans) < k: ans.append(x)
            return ans
            
        ans = [0] * k
        for i in range(k+1): 
            if k - len(nums2) <= i <= len(nums1): 
                val1 = solution_157_2_2(nums1, i)
                val2 = solution_157_2_2(nums2, k-i)
                cand = []
                i1 = i2 = 0
                while i1 < len(val1) or i2 < len(val2): 
                    if val1[i1:] >= val2[i2:]: 
                        cand.append(val1[i1])
                        i1 += 1
                    else: 
                        cand.append(val2[i2])
                        i2 += 1
                ans = max(ans, cand)
        return ans