class Solution:
    def solution_909_1(self, s: str) -> str:
        s = list(s)
        # Big S: O(n)
        result = []
        
        # Logic is capture distinct char with set
        # Remove found char from initial string
        
        # Big O: O(n)
        while len(s) > 0:

            # Big O: O(n log n) Space: O(n)
            smallest = sorted(set(s))
            # Big O: O(s) - reduced set
            for small in smallest:
                result.append(small)
                s.remove(small)
                
            # Big O: O(n log n) Space: O(n)
            largest = sorted(set(s), reverse = True)
            # Big O: O(s) - reduced set
            for large in largest:
                result.append(large)
                s.remove(large)
        
        return ''.join(result)
    
        # Summary:  Big O(n)^2 Space: O(n)