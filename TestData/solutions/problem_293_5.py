class Solution(object):
    def solution_293_5(self, num):
        """
        :type num: int
        :rtype: str
        """
        r  =""
        if num == 0:
            return "0"
        num1 = abs(num)
        while(num1 >0):
            prevnum =  num1
            num1 =num1/7
            l =  num1 * 7
            k = abs(l-prevnum)
            r =   str(k) +  r 
        if num < 0 :
            return "-"  + r
        else : 
            return  r