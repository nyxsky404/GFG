#User function Template for python3

class Solution:
    def arraySortedOrNot(self, arr) -> bool:
        for i in range(0,len(arr)-1):
            if arr[i] > arr[i+1]:
                return False
        return True       
                
#{ 
 # Driver Code Starts
# Importing necessary modules
import sys
from typing import List

# Main function
if __name__ == "__main__":
    input = sys.stdin.read().strip().split("\n")
    t = int(input[0])
    index = 1
    solution = Solution()

    for _ in range(t):
        line = list(map(int, input[index].strip().split()))
        index += 1
        ans = solution.arraySortedOrNot(line)
        print("true" if ans else "false")
        print("~")
# } Driver Code Ends