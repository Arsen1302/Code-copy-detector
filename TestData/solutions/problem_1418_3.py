class Solution:
    def solution_1418_3(self, tickets: List[int], k: int) -> int:
		#Loop through all elements in list only once.  
		
        nums = tickets 
        time_sec = 0
		# save the number of tickets to be bought by person standing at k position
        least_tickets = nums[k]     
		#(3) Any person nums[i] having tickets more than the k pos person, will buy tickets least_tickets times only.
		#(2) Person nums[i] having tickets less than kth person ( nums[i] < least_tickets ), and standing before him(i<k), will be able to buy nums[i] amount.
		#(1) Person nums[i] standing after kth person having more tickets than kth person, will be able to buy one less than the ticket kth person can buy(condition: least_tickets - 1).
        for i in range(len(nums)):                  
            if k < i and nums[i] >= least_tickets :         #(1)
                time_sec += (least_tickets - 1)
            elif nums[i] < least_tickets :                   #(2)
                time_sec += nums[i]
            else:                                            #(3)
                time_sec += least_tickets
				
        return time_sec
        
Please upvote if you find it useful and well-explained!