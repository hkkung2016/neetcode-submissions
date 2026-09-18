class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        longest = 0
        for item in numset:
            if (item - 1) not in numset:
                length = 1
                while (length + item) in numset:
                    length += 1
                longest = max(length, longest)
        return longest