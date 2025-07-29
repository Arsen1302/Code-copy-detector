class Solution:
    def solution_734_4(self, arr1: List[int], arr2: List[int]) -> List[int]:
        ans = []
        carry, i1, i2 = 0, len(arr1), len(arr2)
        while i1 or i2 or carry: 
            if i1: carry += arr1[(i1 := i1-1)]
            if i2: carry += arr2[(i2 := i2-1)]
            ans.append(carry &amp; 1)
            carry = -(carry >> 1)
        while ans and not ans[-1]: ans.pop() # remove leading 0s
        return ans[::-1] or [0]