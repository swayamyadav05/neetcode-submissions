class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for s in strs:
            sortedAnagram = "".join(sorted(s))
            res[sortedAnagram].append(s)
        return list(res.values())

