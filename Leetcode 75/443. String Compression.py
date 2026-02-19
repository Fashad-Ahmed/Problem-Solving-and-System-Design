# https://leetcode.com/problems/string-compression/submissions/1924817417
class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        len_arr = len(chars)
        if (len_arr == 1):
            return
        ans = 0; i = 0
        while i < len_arr:
            letter = chars[i]
            count = 0
            while i < len_arr and chars[i] == letter:
                count += 1
                i += 1
            chars[ans] = letter
            ans += 1
            if count > 1:
                for c in str(count):
                    chars[ans] = c
                    ans += 1
        return ans
