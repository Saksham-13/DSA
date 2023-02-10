class Solution {
public:
    vector<int> rearrangeArray(vector<int>& nums) {
        int n = nums.size();
        vector<int> arr(n,0);
        int i=1, j=0;
        for(auto x : nums)
        {
            if(x<0){
                arr[i]=x;
                i+=2;
            }
            else{
                 
                arr[j]=x;
                j+=2;
            
            }
}
        return arr;
    }
};