class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)
        max_len = 0

        i = 0
        while i < n:
            j = i
            while j < n and s[j] == s[i]:
                j += 1
            max_len = max(max_len, j - i)
            i = j

        from itertools import combinations

        for x, y in combinations("abc", 2):
            diff_map = {0 : -1}
            diff = 0
            start = -1

            for i in range(n):
                if s[i] == x:
                    diff += 1
                elif s[i] == y:
                    diff -= 1
                else:
                    diff = 0
                    diff_map = {0 : i}
                    continue
                
                if diff in diff_map:
                    max_len = max(max_len, i - diff_map[diff])
                else:
                    diff_map[diff] = i
        c_a = c_b = c_c = 0
        diff_map = {(0, 0): -1}

        for i in range(n):
            if s[i] == 'a':
                c_a += 1
            elif s[i] == 'b':
                c_b += 1
            else:
                c_c += 1

            key = (c_b - c_a, c_c - c_a)
            if key in diff_map:
                max_len = max(max_len, i - diff_map[key])
            else:
                diff_map[key] = i

        return max_len
            