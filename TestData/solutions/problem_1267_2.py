class Solution:
    def solution_1267_2(self, box: List[List[str]]) -> List[List[str]]:
        R,C = len(box), len(box[0])
        new_box = [[0 for _ in range(R)] for _ in range(C)]
        
        for r in range(R):
            for c in range(C):
                new_box[c][~r] = box[r][c]   #(2,0) becomes (0,0)  if 2 is the last row.
				
        R,C = C,R
        for c in range(C):
            last = R - 1   # If we find a stone, we move it here
            for r in reversed(range(R)):  # iterate from bottom to top
                if new_box[r][c] == '*':   # if its a barrier, last is now above this barrier
                    last = r - 1
                elif new_box[r][c] == '.': # if its empty, we don't care
                    continue
                elif new_box[r][c] == '#': # we hit a stone. Where do we move it? To last of course.
                    new_box[r][c] = '.'  # set current location to empty as stone is no longer here
                    new_box[last][c] = '#' # stone is now at last place.
                    last -= 1  # decrement last
        return new_box