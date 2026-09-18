class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        longest = 0
        for i, item in enumerate(numset):
            if (item - 1) not in numset:
                length = 1
                while (length + item) in numset:
                    length += 1
                longest = length if length > longest else longest
        return longest