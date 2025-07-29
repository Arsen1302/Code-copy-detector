class Solution:
    def solution_1626_5(self, nums: List[int], k: int) -> int:
        count=0
        n=len(nums)
        
        # Brute Force
        # s=set()
        # for i in range(n):
        #     for j in range(n):
        #         a=nums[i] | nums[j]
        #         b=nums[i] &amp; nums[j]
        #         a_count=bin(a).count('1')
        #         b_count=bin(b).count('1')
        #         if a_count+b_count>=k and (nums[i], nums[j]) not in s:
        #             s.add((nums[i], nums[j]))
        #             count+=1
        # return count
        
        arr=[]
        for num in set(nums):
            arr.append(bin(num).count('1'))
        arr.sort()
        l=0
        r=len(arr)-1
        ans=0
        while l<=r:
            if arr[l]+arr[r]>=k:
                ans+=(r-l)*2 + 1
                r-=1
            else:
                l+=1
        return ans