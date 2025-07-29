class Solution:
    def solution_541_2(self, target: int, position: List[int], speed: List[int]) -> int:
        """
        sort the start position.
        the car behind can only catch up no exceed.
        so if the car start late and speed is faster, it will catch up the car ahead of itself and they become a fleet.
        there is a target(or desitination),so use arrive time to measure. 
        
        start late but arrive ealier means the car is behind and will catch up before arriving the destination.
        
        position  10  8  5  3  0
        distance  2   4  7  9  12
        speed.    2   4  1  3  1
        time.     1   1  7  3  12
                      ^     ^
                      |     |
                     catch  catch up the previous car before target, join the fleet
		stack = [1] , [1],[1,7],[1,7][1,7,12] 			 
                                
        """
        stack = []
        for pos, v in sorted(zip(position, speed),reverse = True):

            dist = target - pos
            time = dist / v 
            
            if not stack:
                stack.append(time)
            elif time > stack[-1]:
                stack.append(time)

        return len(stack)