class Solution:
    def solution_519_5(self, S: str) -> str:
        if "@" in S: # email address
            name, domain = S.lower().split("@")
            return f"{name[0]}*****{name[-1]}@{domain}"
        else: # phone number 
            d = "".join(c for c in S if c.isdigit())
            ans = f"***-***-{d[-4:]}"
            return ans if len(d) == 10 else f"+{'*'*(len(d)-10)}-" + ans