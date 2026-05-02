class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       

        for x,i in enumerate(nums):
            for y,j in enumerate(nums):
                if x != y:
                    if i + j == target:
                        if x > y:
                            return [y, x]
                        return [x, y]
        return []