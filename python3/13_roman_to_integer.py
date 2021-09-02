class Solution:
    '''
    Time: O(N)
    Space: O(1)
    runtime: 74
    memory: 14.4
    '''
    @staticmethod
    def romanToInt(s: str) -> int:
        res = 0
        for idx, num in enumerate(s):
            if num == "I": res += 1
            elif num == "V": res += 5
            elif num == "X": res += 10
            elif num == "L": res += 50
            elif num == "C": res += 100
            elif num == "D": res += 500
            elif num == "M": res += 1000
            else: raise ValueError('The input string contains unrecognizable char.')

            if idx != 0:
                if num == "V" and s[idx-1] == "I": res -= 2
                if num == "X" and s[idx-1] == "I": res -= 2
                if num == "L" and s[idx-1] == "X": res -= 20
                if num == "C" and s[idx-1] == "X": res -= 20
                if num == "D" and s[idx-1] == "C": res -= 200
                if num == "M" and s[idx-1] == "C": res -= 200

        return res

if __name__ == "__main__":
    for i in range(10):
        print(Solution.romanToInt(str(input())))