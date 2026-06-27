class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        output = [1]*n
        left = 1

        for i in range(n) :
            output[i] = left
            left *= nums[i]

        rigth = 1

        for i in range(n-1, -1, -1):
            output[i] *= rigth
            rigth *= nums[i]

        return output