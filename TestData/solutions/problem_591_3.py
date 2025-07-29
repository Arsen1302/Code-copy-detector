class Solution:
    def solution_591_3(self, A: List[int]) -> int:
        
        A = [-math.inf] + A + [-math.inf]
        n = len(A)
        
        st = []
        res = 0
        
        for i in range(n):
            
            while st and A[st[-1]] > A[i]: # monotonic increasing stack
                mid = st.pop()
                left = st[-1] # previous smaller element
                right = i #next smaller element
                
                res += A[mid] * (mid - left) * (right - mid)
            
            st.append(i)
        return res %(10**9 + 7)