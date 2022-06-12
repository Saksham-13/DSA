class Solution:
    def isPalindrome(self, x: int) -> bool:
        check = x
        sum1 = 0
        while(check>0):
            sum1 = sum1*10 + check%10
            check//=10
        return(x==sum1)