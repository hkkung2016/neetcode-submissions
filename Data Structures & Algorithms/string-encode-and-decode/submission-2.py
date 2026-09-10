class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ""
        for i in strs:
            output = output + i + "\n"
        return output

    def decode(self, s: str) -> List[str]:
        return s.split("\n")[0:-1]