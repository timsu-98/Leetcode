class Solution:
    '''
    runtime 51 ms
    memory 14.6 MB
    Time On
    space O1 ?
    '''
    @staticmethod
    def longestCommonPrefix(strs):
        minimum = min(len(x) for x in strs)

        first_str = strs[0]
        prefix = ""
        for idx in range(minimum):
            for compare_str in strs[1:]:
                if first_str[idx]!=compare_str[idx]:
                    return prefix
            prefix += first_str[idx]
        return prefix


if __name__ == "__main__":
    strs = ["dog","racecar","car"]
    print(Solution.longestCommonPrefix(strs))