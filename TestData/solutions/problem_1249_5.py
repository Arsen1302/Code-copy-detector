class Solution:
    def solution_1249_5(self, arr1: List[int], arr2: List[int]) -> int:
        ans = 0
        for i in range(32):
            arr1_set_count = 0
            arr2_set_count = 0
            
            for x in arr1:
                if x&amp;(1<<i) != 0:
                    arr1_set_count ^= 1
            
            for x in arr2:
                if x&amp;(1<<i) != 0:
                    arr2_set_count ^= 1
            if (arr1_set_count &amp; arr2_set_count):
                ans |= (1<<i)
        return ans