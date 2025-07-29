class Solution:
    def solution_230_5(self, s: str) -> str:
        ans = ""

        # words with unique letters
        ans += "0"*(s.count("z"))
        s = s.replace("z","",s.count("z")).replace("e","",s.count("z")).replace("r","",s.count("z")).replace("o","",s.count("z"))
        ans += "2"*(s.count("w"))
        s = s.replace("w","",s.count("w")).replace("t","",s.count("w")).replace("o","",s.count("w"))
        ans += "4"*(s.count("u"))
        s = s.replace("u","",s.count("u")).replace("f","",s.count("u")).replace("o","",s.count("u")).replace("r","",s.count("u"))
        ans += "6"*(s.count("x"))
        s = s.replace("x","",s.count("x")).replace("s","",s.count("x")).replace("i","",s.count("x"))
        ans += "8"*(s.count("g"))
        s = s.replace("g","",s.count("g")).replace("e","",s.count("g")).replace("i","",s.count("g")).replace("h","",s.count("g")).replace("t","",s.count("g"))
        # print(ans)
        # print(s)
        
        #1
        ans += "1"*(s.count("o"))
        s = s.replace("o","",s.count("o")).replace("n","",s.count("o")).replace("e","",s.count("o"))
        
        #3
        ans += "3"*(s.count("r"))
        s = s.replace("r","",s.count("r")).replace("t","",s.count("r")).replace("h","",s.count("r")).replace("e","",s.count("r")*2)
        
        #5
        ans += "5"*(s.count("f"))
        s = s.replace("f","",s.count("f")).replace("i","",s.count("f")).replace("v","",s.count("f")).replace("e","",s.count("f"))
        
        #7
        ans += "7"*(s.count("v"))
        s = s.replace("v","",s.count("v")).replace("s","",s.count("v")).replace("n","",s.count("v")).replace("e","",s.count("v")*2)
        
        #9
        ans += "9"*(s.count("i"))
        s = s.replace("i","",s.count("i")).replace("e","",s.count("i")).replace("n","",s.count("i")).replace("n","",s.count("i")*2)
        
        return "".join(sorted(ans))