class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        ans = []
        for word in words:
            summ = 0
            for ch in word:
                summ += weights[ord(ch) - ord('a')]
            val = summ % 26
            ans.append(chr(ord('z') - val))
        return "".join(ans)