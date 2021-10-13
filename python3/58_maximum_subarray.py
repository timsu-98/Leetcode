class Solution:
    @staticmethod
    def maxSubArray(nums: list[int]) -> int:
        pre_sum = 0 # sum of all the precedent nums
        max_sum = nums[0]
        for i in range(len(nums)):
            sumation = 0
            for j in range(i, len(nums)):
                sumation += nums[j]
                max_sum = max(max_sum, sumation)
        return max_sum


if __name__=="__main__":
    solution = Solution()
    nums = [8,-19,5,-4,20]
    output = Solution.maxSubArray(nums)
    print(output)
                