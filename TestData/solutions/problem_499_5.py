class Solution:
    def solution_499_5(self, cpdomains: List[str]) -> List[str]:
        hashmap=collections.defaultdict(int)
        
        for i in cpdomains:
            port, website=i.split()
            port=int(port)
            
            url=""
            for domain in website.split(".")[::-1]:
                url=domain+url
                hashmap[url]+=port
                url="."+url
            
        print(hashmap.items())
        return [ str(port)+" "+url for url,port in hashmap.items()]