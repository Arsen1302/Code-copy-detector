class Solution:
    def solution_695_3(self, k: int) -> int:
        #edge case
		if k % 2 == 0 or k % 5 == 0: return -1
		
		#keep track of the remainder
        remain, length = 0, 0
        found_so_far = set()
        while remain not in found_so_far:
            found_so_far.add(remain)
            remain = (remain * 10 + 1) % k
            length += 1
        return length if remain == 0 else -1