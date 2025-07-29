class Solution:
    def solution_897_5(self, target) -> bool:
        # Assuming we need to get to all 1s we would need to have the final array to contain all 1s -> sum([]) -> len(target)
        expected_sum = len(target)
        
        # The sum of the array in its current state.
        current_sum = sum(target)
        
        # Min heap to help with the largest number to pull next out. 
        mtarget = [0-x for x in target]

        heapq.heapify(mtarget)

        # loop around assumign that we are reducing current sum to reach expected sum in greedy way.         
        while current_sum > expected_sum:
            # Get the next largest number. 
            max_value = heapq.heappop(mtarget)
            
            # Min heap with negative value, hence flip the value to +ve again. 
            max_value = 0-max_value

            # Assuming that max value was inserted in the place it was the orignal number in that place would need to be first calulated. 
            replacement = max_value - ( current_sum - max_value )
            
            # There are some corner cases and also a test case below that can be dealt with in super fast way if we knew arr_sum_minus_max
            # if exactly 1 then only one reason, the case below. 
            # I added these two cases below after tests failure, it takes mastery to think thse corner cases upfront.:)
            # [1,1000000000]
            
            # If eventually if the diff becomes zero, its a case we would not eventually reach '1's
            arr_sum_minus_max = ( current_sum - max_value )

            if arr_sum_minus_max == 1:
                replacement = 1  
            elif arr_sum_minus_max == 0:
                return False

            # If we realise that the replacement we chose in greedy way can crawl down all the way in small increments, we can optimize that. 
            # An example for the two elements case, below. 
            
            # ......
            # 902 [-900, -2]
            # 900 [-898, -2]
            # 898 [-896, -2]
            # 896 [-894, -2]
            # ......

            if replacement > (current_sum - max_value + 1):
                replacement = replacement - ((replacement // arr_sum_minus_max) * arr_sum_minus_max)
            
            ## If the replacement goes below, 1 declare failure.
            if replacement < 1:
                return False
                
            # Adjust current sum since we chose / acted on the item to be inserted back in place of the pop at the begining of the loop.         
            current_sum = current_sum - max_value + replacement

            # put the replacement back in the min heap. 
            heapq.heappush(mtarget, 0-replacement)

        # Check if we reached the goal. 
        if current_sum == expected_sum:
            return True
        else:
            return False

Runtime: 248 ms, faster than 84.67% of Python3 online submissions for Construct Target Array With Multiple Sums.
Memory Usage: 20 MB, less than 81.02% of Python3 online submissions for Construct Target Array With Multiple Sums.