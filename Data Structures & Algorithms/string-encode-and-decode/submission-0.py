class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = []
        for s in strs:
            encoded.append(f"{len(s)}#{s}")
        return "".join(encoded)

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            # Find the separator '#'
            j = i
            while s[j] != '#':
                j += 1

            length = int(s[i:j])
            i = j + 1

            res.append(s[i:i + length])
            i += length

        return res
