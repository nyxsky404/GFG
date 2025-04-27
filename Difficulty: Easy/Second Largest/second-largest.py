class Solution:
    def getSecondLargest(self, arr):
        large = float('-inf')
        sec_large = float('-inf')
        
        for i in arr:
            if i > large:
                sec_large = large
                large = i
            elif i > sec_large and large != i:
                sec_large = i
        
        if sec_large == float('-inf'):
            return -1
        return sec_large


#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.getSecondLargest(arr)
        print(ans)
        print("~")
# } Driver Code Ends