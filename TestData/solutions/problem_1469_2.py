class Solution:
    def solution_1469_2(self, target: int, maxDoubles: int) -> int:
        # If all maxDoubles are expired then number of -1 operations to go from target to 1 is (target-1)
		# If target is 1 that means we return 0. Since target is 1, we return target-1
        if maxDoubles == 0 or target == 1:
            return target - 1
        subracts = 0 # Considering no -1 operation required initially
        if target%2 != 0: # Target is odd, we must do one -1 operation to make it even
            subracts=1
            target-=1 # Target is now even
        target = target//2
        maxDoubles -= 1 # Since we used a maxDouble operation we have one less /2 operation to work from
        return self.solution_1469_2(target, maxDoubles)+subracts+1
        # we add 1 here as we will do the /2 operation always