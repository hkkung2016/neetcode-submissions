class Solution:

    def encode(self, strs: List[str]) -> str:
        return "\n".join(strs) + "\n" if strs else ""

    def decode(self, s: str) -> List[str]:
        return s.split("\n")[0:-1]