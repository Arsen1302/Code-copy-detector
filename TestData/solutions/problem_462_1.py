class Solution:
def solution_462_1(self, nums: List[int]) -> int:
    
    st = []
    for n in nums:
        if len(st)==0 or st[-1]<=n:
            st.append(n)
        else:
            ma = st[-1]
            while st and st[-1]>n:
                ma = max(ma,st.pop())
            st.append(ma)
    
    return len(st)