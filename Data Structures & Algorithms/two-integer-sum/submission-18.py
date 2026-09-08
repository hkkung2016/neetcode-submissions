class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsdic = dict()
        for i, item in enumerate(nums):
            numsdic[item] = i
        for i, item in enumerate(nums):
            diff = target - item
            if diff in numsdic and numsdic[diff] != i:
                return [i, numsdic[diff]]
        return []