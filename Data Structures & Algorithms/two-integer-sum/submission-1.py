class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numbersSet = {}
        for i in range(len(nums)):
            value = target - nums[i]
            if value in numbersSet:
                return [numbersSet.get(value), i]
            else:
                numbersSet[nums[i]] = i

