class Solution:
		def solution_850_4(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:

			seen = {}

			for i in range(len(s) - minSize + 1):

				check = s[i : i + minSize]

				if check not in seen:

					# we don't need to have conditions for "minSize" and "maxSize"
					# because check is always keeping a size of minSize
					if len(Counter(check)) <= maxLetters:
						seen[check] = 1

				else:
					seen[check] += 1

			return max(seen.values()) if seen else 0