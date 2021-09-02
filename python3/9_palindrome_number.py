class Solution:
    '''
    Using string
    Time: O(N)
    Space: O(1)
    runtime: 64 ms
    memory: 14.3 MB
    '''
    @staticmethod
    def isPalindrome(x: int) -> bool:
        x = str(x)
        for idx in range(len(x) // 2):
            if x[idx] != x[-idx - 1]:
                return False
        return True

class Solution_2:
    '''
    Not using string
    Time: O(N)
    Space: O(1)
    runtime: 
    memory:
    '''
    @staticmethod
    def isPalindrome(x: int) -> bool:
        if x <= 0: return False

        div = 1
        while x >= 10 * div:
            div *= 10
        
        while x:
            if x // div != x % 10: return False
            x = (x % div) // 10
            div = div / 100
        return True


if __name__ == "__main__":
    for i in range(10):
        x = int(input())
        print(Solution_2.isPalindrome(x))
