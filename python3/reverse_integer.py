class Solution: 
    def reverse(self, x: int) -> int:
        import math
        MIN = -214748364
        MAX = 214748364
        num = 0
        while x:
            digit = int(math.fmod(x, 10))
            x = int(x / 10)
            if (num > MAX or (num == MAX and digit >= 7)):
                return 0
            if (num < MIN or (num == MIN and digit <= -8)):
                return 0
            num = num * 10 + digit
        return num
            

if __name__=="__main__":
    solution = Solution()
    print(solution.reverse(int(input())))