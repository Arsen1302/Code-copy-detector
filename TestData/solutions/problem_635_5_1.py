class Solution:
    def solution_635_5_1(self, arr: List[int]) -> bool:
        
        def solution_635_5_2(nums) :
            stack = []
            while nums :
                top = nums.pop(0)

                if stack and 2*stack[0] == top :
                    stack.pop(0)
                else:
                    stack.append(top)
            if not stack :
                return True
            return False
        
        nega = []
        posi = []
        zero = 0
        
        for num in arr :
            if num < 0 :
                nega.append(num)
            elif num > 0 :
                posi.append(num)
            else :
                zero += 1
                
        if zero%2 != 0 or len(nega)%2 != 0 or len(posi)%2 != 0 :
            return False
        
        nega.sort(reverse=True)
        posi.sort()
        return solution_635_5_2(nega) and solution_635_5_2(posi)