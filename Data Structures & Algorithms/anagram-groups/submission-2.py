class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = dict()
        for item in strs:
            temp = [0] * 26
            for i in item:
                temp[ord(i) - ord('a')] += 1
            if tuple(temp) not in d:
                d[tuple(temp)] = [item]
            else:
                d[tuple(temp)].append(item)
        return list(d.values())