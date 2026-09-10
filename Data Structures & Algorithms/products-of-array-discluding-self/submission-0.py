class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total = 1
        ans = []
        zerocount = 0
        for item in nums:
            if item != 0:
                total *= item
            else:
                zerocount += 1
        for item in nums:
            if zerocount == 0:
                ans.append(int(total/item))
            elif zerocount > 1:
                ans.append(0)
            elif item == 0:
                ans.append(total)
            else:
                ans.append(0)
        return ans