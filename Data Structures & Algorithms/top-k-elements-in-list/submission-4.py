class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 1. find frequency of each num (num: frequency)
        # 2. store in somewhere (frequency: num)
        # 3. sort frequency descendingly
        # 4. output top k numbers
        d = defaultdict(int)
        dvalues = defaultdict(list)
        ans = []
        maximum = -1
        for i in nums:
            d[i] += 1 # num: frequency
            if d[i] > maximum:
                maximum = d[i]
        for i, item in d.items():
            dvalues[item].append(i)
        j = maximum
        while j > 0:
            ans = ans + dvalues[j]
            j = j - 1
            if len(ans)>k:
                break
        return ans[0:k]