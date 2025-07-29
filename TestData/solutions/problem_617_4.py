class Solution:
    def solution_617_4(self, stamp: str, target: str) -> List[int]:
        # edge case consideration 
        if stamp == target : 
            return [0]

        # get stamp and target length 
        stamp_length, target_length = len(stamp), len(target)
        result = []
        # keep count and max iter for less overhead calculating and processing valuation queries 
        count = 0 
        max_iter = 10*target_length
        # set of permutation covers of the stamp 
        stamp_covers = set()   
        # inner outer loop of stamp_length and stamp_length - outer length 
        # falls in O(stamp_length)^2 and O(stamp_length) 
        # somewhere in that range 
        for outer_index in range(stamp_length):
            for inner_index in range(stamp_length - outer_index):
                # add a stamp cover of # * outer_index + stamp[outer_index to stamp_length - inner_index] + # * inner_index
                # this builds our stamp set over time to include shifting permutations of stamp as our cover 
                stamp_covers.add('#' * outer_index + stamp[outer_index : stamp_length - inner_index] + '#' * inner_index)
		
        # print(s_covers)

		# finish criteria is back to wild card all 
        done = '#' * target_length
		# post fix positioning is of size target_length - s_length 
        post_fix = target_length - stamp_length 
        # ensure post fix is of the appropriate sizing according to problem 
        if post_fix > max_iter : 
            post_fix = max_iter

        # loop in range up to and including post_fix 
        for index in range(post_fix + 1):
            # if target for index to index + stamp length in stamp covers 
            if target[index: index + stamp_length] in stamp_covers :
                # update target, moving backwards towards our goal, by placing the mask on the target 
                target = target[ : index] + '#' * stamp_length + target[index + stamp_length : ] 
                # add the index to the result 
                result.append(index)
                count += 1 

        # if we are done 
        if target == done :
            # if we are within range of solution 
            if count <= max_iter + 1 : 
                return result[ : : -1]
            else : 
                # otherwise, return false 
                return []
        # if we are not done, but are too long already 
        elif count > max_iter + 1 :
            # return false 
            return []

        # loop backwards at this point 
        for index in range(post_fix, -1, -1) :
            # if we have stamp cover, place stamp cover and append index  
            if target[index : index + stamp_length] in stamp_covers:
                target = target[ : index] + '#' * stamp_length + target[index + stamp_length : ]
                result.append(index)
                count += 1 
        
        # if done, check if in bounds and return as appropriate 
        if target == done :
            if count <= max_iter + 1 : 
                return result[ : : -1]
            else : 
                return [] 
        return []