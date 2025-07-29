class Solution:
    def solution_838_2(self, groupSizes: List[int]) -> List[List[int]]:
        # Step 1 : Categorise using hashmap
		h = {}
        for index,value in enumerate(groupSizes): 
            h[value] = h.get(value,[]) + [index]
        ans = []
		
		# Step 2 : Prepare the groups
        for size in h.keys():
            num_grps = len(h[size])//size # // means integer division
            for x in range(num_grps):
                temp = []
                for j in range(size):
                    temp.append(h[size].pop(0))
                ans.append(temp)
		# Return the answer
        return ans