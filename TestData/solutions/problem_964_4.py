class Solution:
    def solution_964_4(self, target: List[int], n: int) -> List[str]:
        
        target_idx, cur_read_num = 0, 1
        
        stack_operation = []
        
        while target_idx < len(target):
            
            # Push current read number
            stack_operation.append('Push')
            
            if target[target_idx] == cur_read_num:
                # Current read number is what we need, keep it and update target index
                target_idx += 1
            
            else:
                # Pop out unnecessary element
                stack_operation.append('Pop')
                
            # current read number always +1 after each iteration
            cur_read_num += 1
            
        return stack_operation