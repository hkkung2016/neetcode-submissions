class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsdic = dict()
        for i, item in enumerate(nums):
            numsdic[item] = i
        for i, item in enumerate(nums):
            if (target - item) in numsdic and numsdic[target - item] != i:
                return [i, numsdic[target - item]]
        return []