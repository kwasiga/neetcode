class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for word in strs:
            res += str(len(word)) + "$" + word
        return res

    def decode(self, s: str) -> List[str]:
        res = []

        i = 0

        while i < len(s):
            k = i

            while s[k] != "$":
                k += 1
            length = int(s[i:k])
            i = k + 1
            k = i + length

            res.append(s[i:k])
            i = k
        return res


