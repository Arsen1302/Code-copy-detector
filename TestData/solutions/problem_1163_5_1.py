class Solution:
    def solution_1163_5_1(self, n: int) -> List[int]:
		# to check what all numbers have been used
        vis = [False] * (n + 1)
		
		# intermediate array to build the final sequence
        curr_list = [-1] * (2*n - 1)
        li, ans_list = self.solution_1163_5_2(vis, curr_list, 0, n, n)
        return ans_list
        
    def solution_1163_5_2(self, vis, curr_list, curr_ind, n, rem):
		# base conditon which is to check that we have used all the 'n' numbers
        if rem == 0:
            return True, curr_list
		
		# check what index we have to fill in the intermediate array
        while(curr_list[curr_ind] != -1 and curr_ind < 2 * n - 1):
            curr_ind += 1
        ans = False
        ans_list = None
        for i in range(len(vis) - 1, 0, -1):
			addition = i
			
			# special handling of '1'
            if i == 1:
                addition = 0
				
			# only numbers that are not already used and check for feasibility using the constraints given
           if not vis[i] and self.solution_1163_5_3(curr_list, curr_ind, addition, n):
                vis[i] = True
                curr_list[curr_ind] = i
                curr_list[curr_ind + addition] = i
                is_list, li = self.solution_1163_5_2(vis, curr_list, curr_ind + 1, n, rem - 1)
                if is_list:
                    ans = True
                    ans_list = li
                    break
                curr_list[curr_ind] = -1
                curr_list[curr_ind + addition] = -1
                vis[i] = False
        return ans, ans_list
    
    def solution_1163_5_3(self, curr_list, curr_ind, addition, n):
        if curr_ind + addition < 2*n - 1 and curr_list[curr_ind] == -1 and curr_list[curr_ind + addition] == -1:
            return True
        return False