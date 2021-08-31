from typing import List

class Solution_1:
    '''
    runtime = 6198 ms
    memory usage = 14.8 MB
    time complexity O(N^2)
    memory complexity O(1)
    brutal force search
    '''
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        output = None
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    output = [i, j]
        return output

class Solution_2:
    '''
    runtime 720 ms
    memory usage = 15.1 MB
    time complexity O(N)
    memory complexity O(N)
    Using a map to track searched number and if (target - search_num) == current_num, then we got the answer.
    '''
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        output = None
        searched_nums = []
        for i in range(len(nums)):
            if nums[i] in searched_nums:
                output = [searched_nums.index(nums[i]), i]
            else:
                searched_nums.append(target - nums[i])
        return output

class Solution_3:
    '''
    runtime 56 ms
    memory usage 15.2 MB
    time complexity O(N^2)
    memory complexity O(1)
    Also keeps a searched list but more sophisticated. 
    '''
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
        return

if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    solution = Solution_3()
    ans = solution.twoSum(nums, target)
    print(ans)