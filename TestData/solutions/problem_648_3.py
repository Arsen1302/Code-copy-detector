class Solution:
		def solution_648_3(self, n: int, k: int) -> List[int]:
			res = []
			stack = deque((1, num) for num in range(1, 10))
			while stack:
				curr_pos, curr_num = stack.pop()
				if curr_pos == n:
					res.append(curr_num)
				else:
					last_digit = curr_num % 10
					next_pos = curr_pos + 1
					candidates = (last_digit + k, last_digit - k) if k else (last_digit,)
					for digit in candidates:
						if digit in range(10):
							stack.append((next_pos, curr_num * 10 + digit))
			return res