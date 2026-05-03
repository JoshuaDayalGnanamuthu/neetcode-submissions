class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        word = ""
        right = 0

        current_length = 0

        while right < len(s):
            if s[right] not in word:
                word += s[right]
                current_length += 1
                right += 1

            else:
                index = word.index(s[right])
                word = word[index + 1:]
                max_length = max(max_length, current_length)
                current_length = len(word)
        
        max_length = max(current_length, max_length)
        return max_length

        