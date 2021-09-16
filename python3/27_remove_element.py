class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        i = 0
        while i < len(nums):
            if nums[i]==val:
                del nums[i]
            else: 
                i += 1
        print(nums)
        return len(nums)
    
    def removeElement_best(self, nums: list[int], val: int) -> int:
        k = 0
        for i in range(len(nums)):
            if nums[i]!=val:
                nums[k] = nums[i]
                k += 1
        return k

if __name__=="__main__":
    nums = [0,1,2,2,3,0,4,2]
    val = 2
    solution = Solution()
    print(solution.removeElement(nums, val))
