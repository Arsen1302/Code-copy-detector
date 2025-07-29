class Solution:
    def solution_638_5_1(self, cells: List[int], n: int) -> List[int]:
        
        # since the first and the last cell will always be zero after the
        # first day, the array only has 2**(8-2) = 64 states
        # therefore the cells will be repeated after more than 64 days
        #
        # in addition to that the rules are deterministic. So as soon
        # as we encounter our state after one day (Note: not the state
        # of day one, as out cells might be occupied there), we found
        # a cycle and can go on from there.
        
        if not n:
            return cells
        
        cells = solution_638_5_2(cells)
        day1 = str(cells)
        n -= 1
        
        counter = 0
        while n:
            
            # get the new cells
            new_cells = solution_638_5_2(cells)
            n -= 1
            counter += 1
            
            # compare to the day1
            if str(new_cells) == day1:
                # our pattern is repeated and we found the cycle length (counter)
                # therefore we can shorten all cycles from here and just do the
                # leftover steps in the unfinished cycle.
                n = n % counter
            
            cells = new_cells
            
        # the solution does not accept bools
        return map(int, cells)

        
def solution_638_5_2(cells):
    
    # make a new cell
    cells2 = cells.copy()
    
    # iterate over all cells
    # other than the outer ones
    for index in range(1, len(cells)-1):
        cells2[index] = cells[index-1] == cells[index+1]
    cells2[0] = False
    cells2[-1] = False
    
    return cells2