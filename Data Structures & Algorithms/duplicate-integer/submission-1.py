class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        s = set()

        for idx in nums :
            if idx in s :
                return True
            else :
                s.add(idx)
        
        return False 
        