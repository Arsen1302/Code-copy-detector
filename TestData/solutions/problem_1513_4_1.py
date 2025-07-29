class Solution:
    def solution_1513_4_1(self, nums: List[int]) -> List[int]:
        stack = []
        for idx in range(len(nums)):
            cur_num = nums[idx]
            while len(stack) > 0:
                cur_gcd = self.solution_1513_4_2(numA=stack[-1], numB=cur_num)
                if cur_gcd > 1:
                    cur_num = self.solution_1513_4_3(gcd=cur_gcd, numA=stack[-1], numB=cur_num)
                    stack.pop()
                else:
                    break
            stack.append(cur_num)
        return stack
        
    def solution_1513_4_2(self, numA: int, numB: int) -> int:
        while numA > 0 and numB > 0:
            if numA == numB:
                return numA
            if numA > numB:
                numA %= numB
            else:
                numB %= numA
        if numA > 0:
            return numA
        return numB
    
    def solution_1513_4_3(self, gcd: int, numA: int, numB: int) -> int:
        return (numA * numB) // gcd