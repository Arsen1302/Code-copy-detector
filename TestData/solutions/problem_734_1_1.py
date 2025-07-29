class Solution:
    def solution_734_1_1(self, arr1: List[int], arr2: List[int]) -> List[int]:
        ans = list()
        m, n = len(arr1), len(arr2)
        i, j = m-1, n-1
        def solution_734_1_2(a, b):                                         # A helper function to solution_734_1_2 -2 based numbers
            if a == 1 and b == 1:
                cur, carry = 0, -1
            elif (a == -1 and b == 0) or (a == 0 and b == -1):    
                cur = carry = 1
            else:    
                cur, carry = a+b, 0
            return cur, carry                                  # Return current value and carry
        carry = 0
        while i >= 0 or j >= 0:                                # Two pointers from right side
            cur, carry_1, carry_2 = carry, 0, 0
            if i >= 0:
                cur, carry_1 = solution_734_1_2(cur, arr1[i])
            if j >= 0:    
                cur, carry_2 = solution_734_1_2(cur, arr2[j])
            carry = carry_1 + carry_2
            ans.append(cur)
            i, j = i-1, j-1
        ans = [1,1] + ans[::-1] if carry == -1 else ans[::-1]  # Add [1, 1] if there is a carry -1 leftover
        for i, v in enumerate(ans):                            # Remove leading zero and return
            if v == 1:
                return ans[i:]
        else:
            return [0]