class Solution:
    def solution_849_1_1(self, nums: List[int], k: int) -> bool:
        hand = nums
        W = k
        if not hand and W > 0:
            return False
        if W > len(hand):
            return False
        if W == 0 or W == 1: 
            return True
        expectation_map = {}
        # self.count keep track of the numbers of cards that have been successfully counted as a straight,
        # when self.count == len(hand) => All cards are part of a valid straight 
        self.count = 0
        handLength = len(hand)

        #Sort the hand.
        sortedHand = sorted(hand)

        
        """
        This method updates the expectation map in the following way:
            a) If the len(l) == W
                    => We've completed a straight of length W, add it towards the final count
            b) if the next expected number (num+1) is already in the map 
                    => add the list to a queue of hands waiting to make a straight
            c) if expected number (num+1) not in the map 
                    => Add a new expectation key with value as a new queue with this list 
        """
        def solution_849_1_2(expectation_map, num, l, W):
            # If we have W consecutive numbers, we're done with this set, count towards final count
            if len(l) == W:
                self.count += W
            # we need more numbers to make this straight, add back with next expected num 
            else:
                exp = num + 1
                # Some other list is already expecting this number, add to the queue
                if exp in expectation_map:
                    expectation_map[exp].append(l)

                # New expected number, create new key and set [l] as value
                else:
                    expectation_map[exp] = [l]
        
        """
        Very similar to solution_849_1_2. The difference here is we have the first card of the straight and thus we need to handle it correctly (set the value as a list of lists)
        """
        def solution_849_1_3(expectation_map, num):
            exp = num + 1
            # Some other list is already expecting this number, add to the queue
            if exp in expectation_map:
                expectation_map[exp].append([num])
            # New expected number, create new key and set [num] as value
            else:
                expectation_map[exp] = [[num]]
        
        for idx,num in enumerate(sortedHand):
            # A possible straight can be formed with this number
            if num in expectation_map:
                # there are multiple hands waiting for this number
                if len(expectation_map[num]) > 1:
                    # pop the first hand
                    l = expectation_map[num].pop(0)
                    # add num to this hand
                    l.append(num)
                    # Update the expectation map
                    solution_849_1_2(expectation_map, num, l, W)
                
                # there's only one hand expecting this number
                else:
                    # pop the first hand
                    l = expectation_map[num].pop(0)
                    l.append(num)

                    # Important : del the key! There's no other hand expecting this number
                    expectation_map.pop(num) 
                    solution_849_1_2(expectation_map, num, l, W)
                    
            # Nothing is expecting this number, add new expectation to the map
            else:
                solution_849_1_3(expectation_map, num)
                
        return self.count == handLength