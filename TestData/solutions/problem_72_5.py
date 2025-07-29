class Solution:
    def solution_72_5(self, version1: str, version2: str) -> int:
        v1 = version1.split('.') # Divide string version1 into array seperated by "."
        v2 = version2.split('.') # Divide string version2 into array seperated by "."
        m = len(v1)
        n = len(v2)
		# Just take strings at index i from v1 &amp; v2, convert them to integer and check which version is larger. 
		# If an array is already traversed then we may consider the version to be 0. 
        for i in range(max(m, n)):
            i1 = int(v1[i]) if i < m else 0 
            i2 = int(v2[i]) if i < n else 0
            if i1 > i2:
                return 1
            if i1 < i2:
                return -1
        return 0 # Both versions must be same if their was no difference at any point.