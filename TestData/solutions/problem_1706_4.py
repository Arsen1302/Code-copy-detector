class Solution:
    def solution_1706_4(self, nums: List[int]) -> int:
        ans=0       # ans will store the sum of elements which are even and divisible by 3; 
        cnt=0       # cnt will store the number of elements which are even and divisible by 3;       
										 
        for ele in nums:
		# Elements which are divisible by 3 and are even simply means **It must be divisible by 6** So we are checking that in the loop
		# we are adding it to ans if it is divisible by 6 and increase cnt by 1;
            if (ele%6==0):
                ans+=ele;
                cnt+=1;
        if (cnt==0):
            return 0; # if no element is found return 0;
        return (floor(ans/cnt));  # else return the floor value ofaverage that is sum of elements divided by no. of elements