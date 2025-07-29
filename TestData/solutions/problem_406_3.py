class Solution:
    def solution_406_3(self,nums, k):
        n=len(nums)
        left=[0]*n
        right=[0]*n
        p_sum=[0]*n

        sum=0
        #this is calculating the left sum of k-subarray
        #and saving the max(sum of subarray , sum of prev subarray)
        for i in range(len(nums)):
            if i<k:
                sum+=nums[i]
                left[i]=sum
            else:
                sum=sum+nums[i]-nums[i-k]
                left[i]=max(sum , left[i-1])
                
        
        sum=0

        #this is calculating the right sum of k-subarray
        #and saving the max(sum of subarray , sum of prev subarray)
        for i in range(n-1 , -1 , -1):
            if i+k >=n:
                sum+=nums[i]
                right[i]=sum
            else:
                sum=sum-nums[i+k]+nums[i]
                right[i]=max(sum , right[i+1])

        
        #this is calculating the prefix_sum
        for i in range(n):
            if i==0: 
                p_sum[i]=nums[i]
            else:
                p_sum[i]=p_sum[i-1]+nums[i]
        
        # print(left , right , p_sum , left_ind, right_ind)
        
        res_tot=0
        res_ind=[]
        left_sum=0
        left_ind=-1
        right_sum=0
        right_ind=-1
        mid_ind=-1
        
        #here we are trying to find the middle sub-array max((mid -array using prefix-sum) + max-left-array(from our left array)+right(from our right array)) and saving the values of left , right and middle
        for i in range(k , len(nums)-2*k+1):
            t=max(res_tot,left[i-1] + (p_sum[i+k-1]-p_sum[i-1]) + right[i+k])
            if t!=res_tot:
                res_tot=t
                left_sum=left[i-1] 
                right_sum=right[i+k]
                mid_sum= (p_sum[i+k-1]-p_sum[i-1])
                # while( r>i+k):
                #     print('index' , r)
                #     if right_ind[r]==right_ind[r-1]:
                #         r=r-1
                #     else:
                #         break
        
        # print(left_sum ,mid_sum ,  right_sum)
        # print(left , right , p_sum)

        #now using our prefix sum again we are finding the indexes of the values in left , mid and right while checking for non-overlaping indexes using contraints like {abs(k-i-1)>=mid_ind+k and abs(k-i-1)>=left_ind+k}
        for i in range(k-1 , len( p_sum)):
            if k-i-1==0:
                prev_sum=0
            else:
                prev_sum=p_sum[i-k]

            if p_sum[i]-prev_sum==left_sum and left_ind==-1:
                left_ind=abs(k-i-1)

            elif p_sum[i]-prev_sum==mid_sum and mid_ind==-1 and abs(k-i-1)>=left_ind+k:
                mid_ind=abs(k-i-1)
            
            elif p_sum[i]-prev_sum==right_sum and right_ind==-1 and abs(k-i-1)>=mid_ind+k and abs(k-i-1)>=left_ind+k:
                right_ind=abs(k-i-1)
            
            # print(i , left_ind ,mid_ind ,right_ind)
            
        
        res_ind= [left_ind , mid_ind , right_ind]
        
        return res_ind