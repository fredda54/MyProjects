x = 1245421
class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]
print(Solution().isPalindrome(x))