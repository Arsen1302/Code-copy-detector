class Solution:
    def solution_635_2(self, arr: List[int]) -> bool:
        arr.sort(key=abs)  # Sort the array based on the absolute value
        cnt = Counter(arr)  # Count the number of each element in arr
        while cnt:
            x = next(iter(cnt.keys()))  # Get the next unique element x
			# Handle conditionals (written on multiple lines for clarity)
            if 2*x not in cnt or \  # Condition 1: 2x does not exist in arr
					(x == 0 and cnt[x]&amp;1) or \  # Condition 2: Odd number of 0s in arr
					cnt[2*x] < cnt[x]:  # Condition 3: Insufficient 2x to pair with x in arr
                return False
            cnt[2*x] -= cnt[x]  # Remove the number of 2x elements needed for pairing with x
            _ = cnt.pop(x)  # All x paired; remove x entirely (for iteration purposes)
            if cnt[2*x] == 0 and x != 0:
                _ = cnt.pop(2*x)  # Only remove 2x if there are no more 2x left
        return True