class Solution:
    def solution_240_3_1(self, s: str, p: str) -> List[int]:
        
        def solution_240_3_2( s: str, p: str):
            signature, size_p = sum( map(hash,p) ), len(p)
            size_s = len(s)

            if size_s * size_p == 0 or size_p > size_s :
                # Quick response:
                # Reject empty string
                # Reject oversize pattern
                return []

            cur_signature = sum( map( hash, (s[:size_p]) ) )

            for tail_of_window in range( size_p, size_s ):

                head_of_window = tail_of_window - size_p

                if cur_signature == signature:
                    yield head_of_window

                new_char, old_char = s[tail_of_window], s[ head_of_window ]

                cur_signature += ( hash(new_char) - hash(old_char) )

            # handle for last iteration    
            if cur_signature == signature:
                yield ( size_s - size_p )
        
        # -----------------------
        return [ *solution_240_3_2(s, p) ]