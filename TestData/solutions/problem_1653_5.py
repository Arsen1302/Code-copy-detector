class Solution:
    def solution_1653_5(self, garbage: List[str], travel: List[int]) -> int:
        g = m = p = False  # whether each truck should drive until the current house
        time = 0  # total time needed
        
        # starting from the last house and going backwards, we track which trucks should drive until there by looking at the garbage content.
        while len(travel):
            t = travel.pop()  # travel cost to the current house
            s = garbage.pop()  # garbage string for the current house
            
            # if at least one truck was not needed for all houses after the current, check if it is needed in this house (and thus for all previous houses).
            if sum([g, m, p]) < 3:
                if 'G' in s:
                    g = True
                if 'M' in s:
                    m = True
                if 'P' in s:
                    p = True
                        
            # add to the time cost the number of garbage items in this house and the travel costs for the number of tracks that need to drive until here
            time += sum([g, m, p]) * t + len(s)
            
        # add the garbage cost for the initial house, where no driving time is needed
        time = time + len(garbage[0])  
        
        return time