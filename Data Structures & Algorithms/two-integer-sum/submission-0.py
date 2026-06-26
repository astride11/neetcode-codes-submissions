class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i, idx in enumerate(nums):
            elt = target - nums[i]

            if nums[i] in seen:
                return [seen[nums[i]], i]

            seen[elt] = i