class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        for i in range(0, len(nums)):
            product = 1
            for j in range(0, len(nums)):
                if i == j:
                    continue
                product *= nums[j]
            output.append(product)

        return output