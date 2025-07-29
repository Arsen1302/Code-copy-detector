class Solution:
    def solution_265_3_1(self, queryIP: str) -> str:
        
        def solution_265_3_2(ip_string):
            ip_string=ip_string.split(".")
            if(len(ip_string)!=4):
                print(ip_string)
                return False
            valid=True
            for i in ip_string:
                if(i.isdigit() and int(i)>=0 and int(i)<=255 and  str(int(i))==i ):
                    continue
                else:
                    valid=False
                    return valid
            return valid
        
        def solution_265_3_3(ip_string):
            ip6_chars=["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f","A","B","C","D","E","F"]
            ip_string=ip_string.split(":")
            if(len(ip_string)!=8):
                return False
            valid=True
            for i in ip_string:
                if(len(i)>=1 and len(i)<=4 ):
                    for chars in i:
                        if(chars  in ip6_chars):
                            # print(i)
                            continue
                        else:
                            # print(i)
                            valid=False
                            return valid
                            
                else:
                    # print(i)
                    valid=False
                    return valid
            return valid
                
        ### Actual Code
        ip4=""
        ip6=""
        ans=False
        if("." in queryIP):
            ans=solution_265_3_2(queryIP)
            if(ans):
                return "IPv4"
            
        elif(":" in queryIP):
            
            ans=solution_265_3_3(queryIP)
            # print(ans)
            if(ans):
                return "IPv6"
            
        return "Neither"