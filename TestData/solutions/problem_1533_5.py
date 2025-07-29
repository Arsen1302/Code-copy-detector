class Solution(object):
    def solution_1533_5(self, current, correct):
        """
        :type current: str
        :type correct: str
        :rtype: int
        """
        l = current.split(":")
        m = correct.split(":")
        c = 0 
        c+=int(m[0])-int(l[0])
        x = int(m[1])-int(l[1])
        if int(m[1])<int(l[1]):
            c-=1
            x = int(m[1])
            x+=60-int(l[1])
        while x>0:
            if x>=15:
                c+=x//15 
                x=x%15 

            elif x>=5:
                c+=x//5
                x = x%5
            else:
                c+=x 
                x=0 
        return c