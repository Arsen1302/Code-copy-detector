class Solution:
    def solution_1129_3(self, accounts: List[List[int]]) -> int:
	    # Use the variable below to remember the highest sum.
        wealth = 0
        
        for customer in accounts:
		    # The sum() function below can be replaced with another for-loop in order to traverse the nested lists.
			# In this case, however, the function approach makes it simpler.
            s = sum(customer)
            if wealth < s:
                wealth = s
        
        return wealth