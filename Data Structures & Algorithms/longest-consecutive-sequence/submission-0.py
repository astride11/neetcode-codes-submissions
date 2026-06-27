class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)

        longest = 0

        for idx in s :

            if idx - 1 not in s :
                length = 1
                current = idx

                while current + 1 in s :
                    length +=1
                    current += 1

                longest = max(longest, length)

        return longest