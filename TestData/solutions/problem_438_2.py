class Solution:
    def solution_438_2(self, asteroids: List[int]) -> List[int]:
        stack = []
        for asteroid in asteroids:
			# if there's things on the stack, we need to consider if we've got case 4
            while stack and stack[-1] > 0 and asteroid < 0:
				# determine which asteroids are exploding
                if abs(stack[-1]) < abs(asteroid):
                    stack.pop()
					# considered asteroid might still destroy others so continue checking
                    continue
                elif abs(stack[-1]) == abs(asteroid):
                    stack.pop()
                break
			# if nothing on the stack, or cases 1-3, just append
            else:
                stack.append(asteroid)
        return stack