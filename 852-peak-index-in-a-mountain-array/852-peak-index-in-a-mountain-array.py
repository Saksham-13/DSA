class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        start = 0
        end = len(arr)-1
        while(start<=end):


            if(arr[(start+end)//2]>arr[(start+end)//2-1] and arr[(start+end)//2]>arr[(start+end)//2+1]):
                return (start+end)//2
            elif (arr[(start+end)//2]>arr[(start+end)//2 -1]):
                start = (start+end)//2 +1
            else:
                end = (start+end)//2
                