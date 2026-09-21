class Solution:
    def isPalindrome(self, s: str) -> bool:
        # A:65, z:90, a:97, z:122, 0:48, 9:57
        newstr = list()
        for item in s:
            if (ord(item) >= 97 and ord(item) <= 122) or (ord(item) >= 48 and ord(item) <= 57):
                newstr.append(item)
            elif (ord(item) >= 65 and ord(item) <= 90):
                newstr.append(chr(ord(item)+32))
        l = len(newstr)//2 if len(newstr) % 2 == 0 else (len(newstr)//2)+1
        for i in range(l):
            if newstr[i]!=newstr[len(newstr)-i-1]:
                return False
        return True