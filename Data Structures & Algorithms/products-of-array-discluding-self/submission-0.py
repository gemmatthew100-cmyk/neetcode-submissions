class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:    
        invalid_index = 0
        output = []
        for i in range(len(nums)):
            invalid_index = i
            res = 1
            for j in range(len(nums)):
                if j == invalid_index:
                    continue
                res = res * nums[j]
            output.append(res)
        return output
                

        