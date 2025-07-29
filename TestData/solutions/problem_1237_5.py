class Solution:
    def solution_1237_5(self, nums1: List[int], nums2: List[int]) -> int:
        nums3 = sorted(nums1)
        n = [-1 for i in range(len(nums1))] # i = index in nums1 | n[i] = index in nums3 | the best diff for every nums1[i] is nums3[n[i]] - nums2[i]
        pos = -math.inf
        m_diff, s = 0, 0
        for i in range(len(nums2)):
            m1 = bisect.bisect_left(nums3, nums2[i]) # m1 = upper and m2 = lower
            if m1 >= len(nums1): # in case m1 is outside the array's range
                m1 = len(nums1)-1
            m2 = m1 - 1
            val = abs(nums1[i] - nums2[i])
            if abs(nums3[m1] - nums2[i]) < val:
                val = abs(nums3[m1] - nums2[i])
                n[i] = m1
            if m2 >= 0:
                if abs(nums3[m2] - nums2[i]) < val:
                    n[i] = m2
        for i in range(len(nums3)): #get the maximum change in difference and the position to change in order to get that
            currentDiff = abs(nums1[i] - nums2[i])
            newDiff = abs(nums3[n[i]] - nums2[i])
            if n[i] != -1 and currentDiff > newDiff and currentDiff - newDiff > m_diff:
                m_diff = currentDiff - newDiff
                pos = i
        if pos != -math.inf: nums1[pos] = nums3[n[pos]] # no change to be made if pos == -inf
        for i in range(len(nums1)):
            s += abs(nums1[i] - nums2[i])
        return s % (10**9 + 7)