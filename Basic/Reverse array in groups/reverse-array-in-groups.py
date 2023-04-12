#User function template for Python

class Solution:    
    #Function to reverse every sub-array group of size k.
    def reverseInGroups(self, a, n, k):
        # code here
        def rev(a,l,h):
            while(l<h):
                a[l],a[h]=a[h],a[l]
                l+=1
                h-=1
                
        l=0
        h=0
        for i in range(n):
            if i%(k)==0 and i!=0:
                #print('index',i)
                h=i-1
                rev(a,l,h)
                l=i
        h=n-1
        rev(a,l,h)
        
        

#{ 
 # Driver Code Starts
#Initial template for Python

import math
def main():
    T=int(input())
    while(T>0):
        nk=[int(x) for x in input().strip().split()]
        N=nk[0]
        K=nk[1]
        arr=[int(x) for x in input().strip().split()]
        
        ob = Solution()
        ob.reverseInGroups(arr,N,K)
        for i in arr:
            print(i,end=" ")
        print()
        T-=1

if __name__=="__main__":
    main()




# } Driver Code Ends