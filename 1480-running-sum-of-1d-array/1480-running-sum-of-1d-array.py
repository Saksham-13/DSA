class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sum = 0
        b= []
        for i in nums:
            sum += i
            b.append(sum)
        return b
            