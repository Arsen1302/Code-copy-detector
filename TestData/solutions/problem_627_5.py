class Solution:
    def solution_627_5(self, pushed: List[int], popped: List[int]) -> bool:
        
        stack, pushed, popped = [], collections.deque(pushed), collections.deque(popped)
                        
        while pushed or popped:
            try:
                while not stack or stack[-1] != popped[0]:
                    stack += [pushed.popleft()]
                stack.pop(), popped.popleft()   
            except:
                return False
        
        return True