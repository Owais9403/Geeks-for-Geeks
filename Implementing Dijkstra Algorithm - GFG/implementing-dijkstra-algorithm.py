class Solution:

    #Function to find the shortest distance of all the vertices
    #from the source vertex S.
    def dijkstra(self, n, a, s):
        dis=[int(1e9) for i in range(n)]
        q=[[s,0]]
        dis[s]=0
        while(len(q)):
            node,d=q.pop(0)
            #print(node)
            for i in a[node]:
                n1,w=i
                if dis[n1]>d+w:
                    dis[n1]=d+w
                    q.append([n1,d+w])
        return dis
            
            
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        V,E = map(int,input().strip().split())
        adj = [[] for i in range(V)]
        for i in range(E):
            u,v,w = map(int,input().strip().split())
            adj[u].append([v,w])
            adj[v].append([u,w])
        S=int(input())
        ob = Solution()
        
        res = ob.dijkstra(V,adj,S)
        for i in res:
            print(i,end=" ")
        print()
# } Driver Code Ends