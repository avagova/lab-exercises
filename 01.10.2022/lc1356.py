class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        res = {}
        for i in arr:
            c = bin(i)[2:].count('1')
            if c not in res:
                res[c] = [i]
            else:
                res[c].append(i)
        r = []
        for i in sorted(res.keys()):
            r += sorted(res[i])
        return r
