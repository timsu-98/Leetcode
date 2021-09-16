class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        last = None
        idx = 0
        while idx < len(nums):
            if nums[idx]!=last:
                last = nums[idx]
                idx += 1
            else:
                del nums[idx]
            print(nums)
        return len(nums)

    def removeDuplicates_best(self, nums: list[int]) -> int:
        '''
        
        '''
        l = r = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[l] = nums[i]
                l += 1
            else:
                r += 1
        return l

if __name__=="__main__":
    solution = Solution()
    input = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    k = solution.removeDuplicates(input)
    print(k)