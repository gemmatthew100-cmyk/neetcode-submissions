class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        arr = []
        duplicate = False
        for num in nums:
            if num not in arr:
                arr.append(num)
            else:
                duplicate = True
                return duplicate
        return duplicate

