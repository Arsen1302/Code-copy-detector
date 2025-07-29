class Solution:
    def solution_1371_1(self, changed: List[int]) -> List[int]:
        
        """
        The idea is to:
            1st sort the numbers
            2nd Create a counter to save the frequency of each number
            3nd iterate the array and for each number check if the double exists.
            4rd after taking len(changed) // 2 numbers return the answer
            
        Time complexity: O(nlog(n)) 
        Space complexity: O(n)
        
        """
        
        
        if len(changed) % 2 != 0: # If there are not even amount the numbers there is no solution.
            return []
        
        changed.sort()
        
        c = Counter(changed) # The counter is needed because we have 0s
        
        answer = []
        for num in changed:
            if num in c and c[num] >= 1: # Check if the number is available (we may have taken it before)
                c[num] -= 1 # we mark the number as used by decreasing the counter (only needed for the zeros)
                if (num * 2) in c and c[(num * 2)] >= 1: # Take the one that doubles it if exists
                    answer.append(num)
                    c[num*2] -= 1 # The number has been taken.
            
            if len(answer) == len(changed) // 2:
                return answer
        
        return []