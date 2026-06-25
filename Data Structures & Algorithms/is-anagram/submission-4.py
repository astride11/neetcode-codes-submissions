class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t) :
            return False

        freq = {}

        for s_idx in s:
            freq[s_idx] = freq.get(s_idx, 0) + 1

        for t_idx in t :
            if t_idx not in freq :
                return False 

            freq[t_idx] -=1

            if freq[t_idx] == 0 :
                del freq[t_idx]

        return len(freq) == 0