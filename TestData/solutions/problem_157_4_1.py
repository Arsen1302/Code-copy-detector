class Solution:
    def solution_157_4_1(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        m = len(nums1)
        n = len(nums2)
        dp = {}
        
        # get the max number string with "length" from index "i" in nums1 and index "j" in nums2
        # using number string to easy to compare
        def solution_157_4_2(i, j, length):
            if length == 0:
                return ""
            
            # using memoization to optimize for the overlapping subproblems
            key = (i, j, length)
            if key in dp:
                return dp[key]
            
            # greedy to find the possible max digit from nums1 and nums2
            # 1) bigger digit in the higher position of the number will get bigger number
            # 2) at the same time, we need to ensure that we still have enough digits to form a number with "length" digits
            
            # try to find the possible max digit from index i in nums1
            index1 = None
            for ii in range(i, m):
                if (m - ii + n - j) < length:
                    break
                if index1 is None or nums1[index1] < nums1[ii]:
                    index1 = ii
            
            # try to find the possible max digit from index j in nums2
            index2 = None
            for jj in range(j, n):
                if (m - i + n - jj) < length:
                    break
                if index2 is None or nums2[index2] < nums2[jj]:
                    index2 = jj
                    
            maxNumberStr = None
            if index1 is not None and index2 is not None:
                if nums1[index1] > nums2[index2]:
                    maxNumberStr = str(nums1[index1]) + solution_157_4_2(index1 + 1, j, length - 1)
                elif nums1[index1] < nums2[index2]:
                    maxNumberStr = str(nums2[index2]) + solution_157_4_2(i, index2 + 1, length - 1)
                else:
                    # get the same digit from nums1 and nums2, so need to try two cases and get the max one 
                    maxNumberStr = max(str(nums1[index1]) + solution_157_4_2(index1 + 1, j, length - 1), str(nums2[index2]) + solution_157_4_2(i, index2 + 1, length - 1))
            elif index1 is not None:
                maxNumberStr = str(nums1[index1]) + solution_157_4_2(index1 + 1, j, length - 1)
            elif index2 is not None:
                maxNumberStr = str(nums2[index2]) + solution_157_4_2(i, index2 + 1, length - 1)
            
            dp[key] = maxNumberStr
            return maxNumberStr

        result_str = solution_157_4_2(0, 0, k)
        
        # number string to digit array
        result = []
        for c in result_str:
            result.append(int(c))
        
        return result