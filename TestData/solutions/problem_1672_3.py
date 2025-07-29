class Solution:
    def solution_1672_3(self, s: str) -> int:
        st = []
        c = 0
        for i in s:
            if not st:
                st.append(i)
            else:
                if i>st[-1] and ord(i) == ord(st[-1]) + 1:
                    st.append(i)
                else:
                    c = max(c,len(st))
                    st = [i]
        return max(c,len(st))