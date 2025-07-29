class Solution:
    def solution_1294_3_1(self, s: str, p: str, removable: List[int]) -> int:
    # You want to choose an integer k (0 <= k <= removable.length) such that, after removing k characters from s using the first k indices in removable.
    # as usual we can search through the answer.
    # we have to use a "seen" set. So we can skip all the "K" removable index. Look at 2nd Example 
	
        left, right = 0, len(removable)
        # right can be len of removable as we can remove all the elements to check
        lenS, lenP = len(s), len(p)
		
		# solution_1294_3_2 : Is "p" still a subsequence of "s"?  After removing of 1st "K or Target" characters
        def solution_1294_3_2(target):
            seen = set(removable[:target])                # contains 1st "K/TARGET" indices
            if target == 0:                                          # always True given in problem itself
                return True
            sIndx,pIndx = 0, 0
            while sIndx < lenS and pIndx < lenP:     # basic check matching stings chr by indexes.
                if sIndx in seen:
                    pass                                                # if this sIndx is in Seen so skip it
                elif s[sIndx] == p[pIndx]: 
                    pIndx += 1                                     # if chr matched pIndx is increased
                sIndx += 1
            return pIndx == lenP                             # return true if still Subsequence else False


        while left <= right:
            mid = left + ((right-left)//2)
            if solution_1294_3_2(mid):                 # if after removing 1st "mid" number of index frpm removable.
                left = mid + 1                     # for True : left can we our answer but we want max so increase it.
            else:
                right = mid - 1                   # for False : this mid is False. So check for Lower Value of mid/K.
        return right                                # return right Answer.