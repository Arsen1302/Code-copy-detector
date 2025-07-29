class Solution:
    def solution_611_1_1(self, emails: List[str]) -> int:
        def solution_611_1_2(email):
            local, domain = email.split('@')
            local = local.split('+')[0].replace('.',"")
            return f"{local}@{domain}"
        
        return len(set(map(solution_611_1_2, emails)))