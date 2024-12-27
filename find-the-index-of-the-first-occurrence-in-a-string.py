class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack)-len(needle)+1):
            matched = i
            for j in range(len(needle)):
                if haystack[i+j]!=needle[j]:
                    matched = -1
                    break
            if matched != -1:
                return matched

        return -1
                        
