class Solution:
    def solution_1100_5(self, releaseTimes: List[int], keysPressed: str) -> str:
        maxTime = float("-inf")
        maxChar = ""
        for i in range(len(keysPressed)):
			# the first one is alwasys the specified release time
            if i==0:
                time = releaseTimes[i]
			# everything after requires a difference in times
			# releasedTimes[i+1] >= releasedTimes[i]
            else:
                time = releaseTimes[i] - releaseTimes[i-1]
			
            if time > maxTime:
                maxTime = time
                maxChar = keysPressed[i]
			# comparing chars, operators allow for lexicographical comparison
            elif time == maxTime and maxChar < keysPressed[i]:
                maxChar = keysPressed[i]
				
		# time complexity : O(N) where N=len(keys)=len(releasedTimes)
		# space complexity: O(1)
        return maxChar