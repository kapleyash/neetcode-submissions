class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))

    #    seen = set()
    #     for i in range(len(nums)):
    #         if nums[i] in seen:
    #             return True
    #         seen.add(nums[i])
    #     return False
