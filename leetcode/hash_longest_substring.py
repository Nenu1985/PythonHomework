class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = maxLength = 0
        usedChar = {}
        
        for i, char in enumerate(s):
            if char in usedChar and start <= usedChar[char]:
                start = usedChar[char] + 1
            else:
                maxLength = max(maxLength, i - start + 1)

            usedChar[char] = i

        return maxLength


if __name__ == '__main__':
    s = Solution()
    print(s.lengthOfLongestSubstring('dvdf')) # 3
    print(s.lengthOfLongestSubstring('bbbb'))  # 1
    print(s.lengthOfLongestSubstring('pwwer'))  # 3
    print(s.lengthOfLongestSubstring("abcabcbb"))  # 3
    print(s.lengthOfLongestSubstring("bbtablud"))  # 6
    print(s.lengthOfLongestSubstring("ckilbkd"))  # 5
    print(s.lengthOfLongestSubstring("bpfbhmipx"))  # 7
    print(s.lengthOfLongestSubstring("jbpnbwwd"))  # 4

