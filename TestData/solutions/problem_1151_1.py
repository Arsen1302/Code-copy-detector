lass Solution:
    def solution_1151_1(self, s: str) -> str:
        #count of 0
        c=0
        #final ans string will contain only one zero.therefore shift the first 0  to c places.Initialize ans string with all 1s
        lst=["1"]*len(s)
        for i in range (0,len(s)):
            if s[i]=="0":
                c+=1
        for i in range (0,len(s)):
		#finding the ist 0
            if s[i]=="0":
                lst[i+c-1]="0"
                return "".join(lst)
        return s