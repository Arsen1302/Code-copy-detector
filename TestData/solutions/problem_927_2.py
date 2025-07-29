class Solution:
    # define direction identifiers
    left, right, up, down = 0, 1, 2, 3
    
    # define possible directions to move from a given street
    moves = {
        1: {left, right},
        2: {up,   down},
        3: {left, down},
        4: {down, right},
        5: {left, up},
        6: {up,   right}
    }
    
    # defind offsets x, y offsets for each direction
    offsets = {
        left:  ( 0, -1, right), # y offset, x offset, move to return to previous position
        right: ( 0,  1, left),
        up:    (-1,  0, down),
        down:  ( 1,  0, up)
    }
        
    def solution_927_2(self, grid: List[List[int]]) -> bool:
        if len(grid) == 1 and len(grid[0]) == 1:
            return True
        
        # on the start we can possibly move only to right and down
        # so there are only two possible paths which can lead as to the final position
        for direction in [Solution.right, Solution.down]:
            cur_x, cur_y = 0, 0
            while 1:
                y_offset, x_offset, reverse_move = Solution.offsets[direction]
                cur_x += x_offset
                cur_y += y_offset
                
                # break if current road leads us to out of grid
                if not (0 <= cur_x < len(grid[0]) and 0 <= cur_y < len(grid)):
                    break
                # break if current road leads us to incompatible road
                if not reverse_move in Solution.moves[grid[cur_y][cur_x]]:
                    break
                
                # we are in the infinite loop
                if (cur_x, cur_y) == (0, 0):
                    break
                
                # define next direction
                direction = [i for i in Solution.moves[grid[cur_y][cur_x]] if i != reverse_move][0]
                if (cur_x, cur_y) == (len(grid[0]) - 1, len(grid) - 1):
                    return True
        return False