from collections import defaultdict, deque

class Solution:
    def minJumps(self, nums):
        n = len(nums)
        mx = max(nums)

        spf = list(range(mx + 1))

        for i in range(2, int(mx ** 0.5) + 1):
            if spf[i] == i:
                for j in range(i * i, mx + 1, i):
                    if spf[j] == j:
                        spf[j] = i

        def get_factors(x):
            factors = set()

            while x > 1:
                p = spf[x]
                factors.add(p)

                while x % p == 0:
                    x //= p

            return factors

        bucket = defaultdict(list)

        for i, val in enumerate(nums):
            for p in get_factors(val):
                bucket[p].append(i)

        q = deque([(0, 0)])
        visited = {0}

        while q:
            i, steps = q.popleft()

            if i == n - 1:
                return steps

            for ni in [i - 1, i + 1]:
                if 0 <= ni < n and ni not in visited:
                    visited.add(ni)
                    q.append((ni, steps + 1))

            if nums[i] > 1 and len(get_factors(nums[i])) == 1 and nums[i] in get_factors(nums[i]):
                p = nums[i]

                for ni in bucket[p]:
                    if ni not in visited:
                        visited.add(ni)
                        q.append((ni, steps + 1))

                bucket[p].clear()

        return -1