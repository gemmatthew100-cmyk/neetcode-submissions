class Solution:
    def isPalindrome(self, s: str) -> bool:
        removed_alnum_st = "".join(filter(str.isalnum, s))
        cleaned_st = removed_alnum_st.lower()
        if cleaned_st == cleaned_st[::-1]:
            return True
        return False
