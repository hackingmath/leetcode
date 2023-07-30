def maxArea(height):
    output = 0
    #if len(height)
    for i in range(len(height)):
        print("i:",i)
        for j in range(len(height) - 1, i, -1):
            print("j:",j)
            h = min(height[i], height[j])
            w = j - i
            output = max(output, h * w)
    return output

print(maxArea([1,8,6,2,5,4,8,3,7]))

"""
Even my C++ brute force solution timed out:
    int maxArea(vector<int>& height) {
        int n = height.size();
        int output = 0;
        for (int i=0;i<n;++i){
            for (int j=n-1;j>i;--j){
                int h=min(height[i],height[j]);
                int w = j-i;
                output = max(output, h * w);
            }
        }
        return output;
    }
    
    This one didn't, with one while loop instead of nested loops:
    int maxArea(vector<int>& height) {
        int n = height.size();
        int output = 0;
        int i = 0;
        int j = n-1;
        while (i<j){
            int a=min(height[i],height[j])*(j-i);
            
            output = max(output, a);
            if (height[i]<height[j]){
                i++;
            } else {
                j--;
            }
        }
        return output;
    }
    """