class Solution:
    def maxScore(self, s: str) -> int:
        max_count = 0
        for i in range(len(s)):
            left_sublist = s[0:i]
            right_sublist = s[i::]
            if len(left_sublist) == 0 or len(right_sublist) == 0:
                continue
            else:
                l_count, r_count = 0, 0
                for j in left_sublist:
                    if j == "0":
                        l_count += 1
                for k in right_sublist:
                    if k == "1":
                        r_count += 1
                total = l_count + r_count
                if total > max_count:
                    max_count = total
        return max_count
