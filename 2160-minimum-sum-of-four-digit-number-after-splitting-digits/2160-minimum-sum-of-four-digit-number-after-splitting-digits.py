class Solution:
    def minimumSum(self, num: int) -> int:
        s = [int(x) for x in str(num)]
        s.sort()
        su = s[0]*10+s[1]*10+s[2]+s[3]
        return su