class Solution:
    def solution_1441_3_1(self, nums: List[int]) -> int:
        mon = monotonicStack()
        
        # for each element, check in how many sub-arrays arrays, it can be max
        # find the prev and next greater element

        # for each element, check in how many sub-arrays arrays, it can be min
        # find the prev and next smaller element
        
        nse_l = mon.solution_1441_3_5(nums)
        nse_r = mon.solution_1441_3_4(nums)
        nge_l = mon.solution_1441_3_3(nums)
        nge_r = mon.solution_1441_3_2(nums)
        
        ans = 0
        
        for idx in range(len(nums)):
            smaller_left, smaller_right = nse_l[idx], nse_r[idx]
            greater_left, greater_right = nge_l[idx], nge_r[idx]
            
            if smaller_right == -1:
                smaller_right = len(nums)
            if greater_right == -1:
                greater_right = len(nums)
            
            min_val = (idx - smaller_left) * (smaller_right - idx) * nums[idx]
            max_val = (idx - greater_left) * (greater_right - idx) * nums[idx]
            
            ans += (max_val - min_val)
        return ans
        
class monotonicStack:
    def solution_1441_3_2(self,arr):
        ans = [None] * len(arr)
        stack = []
        for idx in range(len(arr)-1,-1,-1):
            while stack and arr[stack[-1]] < arr[idx]:
                stack.pop()
            if not stack:
                #no greater element
                ans[idx] = -1
            else:
                ans[idx] = stack[-1]
            stack.append(idx)
        return ans
                
    def solution_1441_3_3(self,arr):
        ans = [None] * len(arr)
        stack = []
        for idx in range(len(arr)):
            while stack and arr[stack[-1]] <= arr[idx]:
                stack.pop()
            if not stack:
                #no greater element
                ans[idx] = -1
            else:
                ans[idx] = stack[-1]
            stack.append(idx)
        return ans 
                
    def solution_1441_3_4(self,arr):
        ans = [None] * len(arr)
        stack = []
        for idx in range(len(arr)-1,-1,-1):
            while stack and arr[stack[-1]] > arr[idx]:
                stack.pop()
            if not stack:
                #no smaller element
                ans[idx] = -1
            else:
                ans[idx] = stack[-1]
            stack.append(idx)
        return ans 
        
    def solution_1441_3_5(self,arr):
        ans = [None] * len(arr)
        stack = []
        for idx in range(len(arr)):
            while stack and arr[stack[-1]] >= arr[idx]:
                stack.pop()
            if not stack:
                #no smaller element
                ans[idx] = -1
            else:
                ans[idx] = stack[-1]
            stack.append(idx)
        return ans