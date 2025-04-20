#{ 
 # Driver Code Starts

# } Driver Code Ends

#User function Template for python3
class Solution:
    def findTarget(self, arr, target):
        i = 0
        j = len(arr) - 1
        n = len(arr)
        
        while i <= j:
            mid = (i+j)//2
            
            next = (mid + 1)% n
            prev = (mid + n - 1)% n
            
            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                if arr[prev] == target:
                    return (prev)
                else:
                    i = mid + 1
            else:
                if arr[next] == target:
                    return (next)
                else:
                    j = mid - 1
                
        return -1
                


#{ 
 # Driver Code Starts.

if __name__ == "__main__":
    t = int(input())  # Number of test cases

    for _ in range(t):
        arr = list(map(int, input().strip().split()))  # Read the array
        target = int(input().strip())  # Read the target

        sln = Solution()
        ans = sln.findTarget(arr, target)
        print(ans)
        print("~")
# } Driver Code Ends