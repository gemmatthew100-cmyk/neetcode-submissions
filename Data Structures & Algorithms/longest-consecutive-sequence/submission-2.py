class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        max_container = []

        for i in range(len(nums)):
            curr_container = []
            curr_container.append(nums[i])
            start = 0
            for j in range(len(nums)):
                if nums[j] == curr_container[start] + 1:
                    start += 1
                    curr_container.append(nums[j])
            if len(curr_container) > len(max_container):
                max_container = curr_container
        return len(max_container)