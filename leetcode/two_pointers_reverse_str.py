from typing import List


        
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        p1 = 0
        p2 = len(s) - 1
        
        while p1 <= p2:
            s[p1], s[p2] = s[p2], s[p1]
            p1 += 1
            p2 -= 1
        return s


class ReverseSolution:
    result = []
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def helper(l, r, s):
            if l >= r:
                return s
            s[l], s[r] = s[r], s[l]
            return helper(l+1, r-1, s)
        helper(0, len(s)-1, s)


if __name__ == '__main__':
    s = Solution()
    print(s.reverseString(["h","e","l","l","o"]))  # ["o","l","l","e","h"]