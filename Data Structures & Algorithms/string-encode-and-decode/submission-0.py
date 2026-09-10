class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ""
        for i in strs:
            output = output + i + "\n"
        return output

    def decode(self, s: str) -> List[str]:
        output = s.split("\n")
        return output[0:-1]