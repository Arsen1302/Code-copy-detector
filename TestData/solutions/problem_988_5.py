class Solution:
        #two pointers approach
        def solution_988_5(self, nums: List[int], n: int) -> List[int]:
                #initialise the l pointer to 0th index
                l = 0 
                #initialise the r pointer to middle index
                r = len(nums)//2
                #create the new list (res)
                res = []
                #condition breaks when l pointer reaches middle index 
                #and r pointer reaches the last index
                while l < len(nums)//2 and r < len(nums):
                        #add the element at l pointer to res -->list
                        res.append(nums[l])
                        #after adding increase the l pointer by 1
                        l = l + 1
                        #add the element at r pointer to res-->list
                        res.append(nums[r])
                        #after adding increase the r pointer by 1
                        r = r +1
        
                #after breaking while loop return res--> list        
                return res