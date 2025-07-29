class Solution:
    def solution_541_4(self, target: int, position: List[int], speed: List[int]) -> int:
        
        # Sort in reverse order of the car w.r.t position
        ps = sorted(list(zip(position, speed)), key = lambda x: x[0], reverse=True)
        
        # Find timestamp of each car reaching the target
        ts = [(target-p)/s for p, s in ps]
        
        # Main logic
        stack = []
        for t in ts:
            
            # Add to stack if stack is empty, or
            # the car ahead of the current car has
            # already reach the target
            if not stack or stack[-1] < t:
                stack.append(t)
        
        # return total no. of fleets
        return len(stack)