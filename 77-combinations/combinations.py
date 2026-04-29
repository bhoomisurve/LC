class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def bt(s, p):
            if len(p) == k:
                res.append(p[:])
                return
            for i in range(s, n + 1):
                p.append(i)
                bt(i + 1, p)
                p.pop()
        bt(1,[])
        return res