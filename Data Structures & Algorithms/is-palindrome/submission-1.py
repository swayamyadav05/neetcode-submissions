class Solution:
    def isPalindrome(self, s: str) -> bool:
        # newStr = ""
        # for c in s:
        #     if c.isalnum():
        #         newStr += c.lower()
        newStr = "".join([c.lower() for c in s if c.isalnum()])
        return newStr == newStr[::-1]

# TC = O(n)
# SC = O(n)