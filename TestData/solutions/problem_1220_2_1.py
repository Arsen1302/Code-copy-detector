class Solution:
    def solution_1220_2_1(self, nums: List[int], k: int) -> int:
        
        N = len(nums)
        
        def solution_1220_2_2():
            
            i = 0
            left=[-1]*N
            stack=[]
            for i in range(N):
                while stack and nums[stack[-1]] >= nums[i]:
                    stack.pop()
                if stack:
                    left[i] = stack[-1]
                stack.append(i)
            
            return left
            
        
        def solution_1220_2_3():
            right=[N]*N
            stack=[]
            for i in range(N-1,-1,-1):
                while stack and nums[stack[-1]] >= nums[i]:
                    stack.pop()
                if stack:
                    right[i] = stack[-1]
                stack.append(i)
            
            return right
        
        left = solution_1220_2_2()
        right = solution_1220_2_3()
        # print(left,right)
        N = len(left)
        ans=-1
        for i in range(N):
            if left[i]+1 <= k <= right[i]-1:
                ans = max(ans,(right[i]-left[i]-1)*nums[i])
                # print(i,ans)
        return ans