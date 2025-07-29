class Solution:
    def solution_1231_5(self, c: str) -> bool:
        if c[0]=="a" and int(c[-1])%2==0:
            return True
        if c[0]=="b" and int(c[-1])%2==1:
            return True
        if c[0]=="c" and int(c[-1])%2==0:
            return True
        if c[0]=="d" and int(c[-1])%2==1:
            return True
        if c[0]=="e" and int(c[-1])%2==0:
            return True
        if c[0]=="f" and int(c[-1])%2==1:
            return True
        if c[0]=="g" and int(c[-1])%2==0:
            return True
        if c[0]=="h" and int(c[-1])%2==1:
            return True
        return False