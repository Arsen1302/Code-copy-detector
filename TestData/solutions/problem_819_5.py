class Solution:
    def solution_819_5(self, nums: List[int], k: int) -> int:
        stack=[]
        preOdd=True
        for i in nums:
            if i%2==1:
                if preOdd:
                    stack.append(1)
            else:
                if preOdd:
                    stack.append(2)
                else:
                    stack[-1]+=1
            preOdd=i%2==1
        if preOdd:
            stack.append(1)

        return sum([stack[j]*stack[j+k] for j in range(len(stack)-k)])