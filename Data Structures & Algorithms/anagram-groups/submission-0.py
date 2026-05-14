class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for s in strs:
            sortAnagram = "".join(sorted(s))
            res[sortAnagram].append(s)
        return list(res.values())