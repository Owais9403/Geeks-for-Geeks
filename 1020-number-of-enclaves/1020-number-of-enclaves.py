class Solution:
    def numEnclaves(self, a: List[List[int]]) -> int:
        n=len(a)
        m=len(a[0])
        vis=[]
        for i in range(n):
            vis.append([0 for i in range(m)])
        d1=[0,1,-1,0]
        d2=[1,0,0,-1]
        def dfs(i,j):
            #print(i,j)
            if vis[i][j]==1:
                return
            vis[i][j]=1
            for k in range(4):
                x=i+d1[k]
                y=j+d2[k]
                
                if x>=0 and x<n and y>=0 and y<m and a[x][y]==1:
                    dfs(x,y)
            
        for i in range(n):
            if a[i][0]==1 and vis[i][0]==0:
                dfs(i,0)
            if a[i][m-1]==1 and vis[i][m-1]==0:
                dfs(i,m-1)
        for i in range(m):
            if a[0][i]==1 and vis[0][i]==0:
                dfs(0,i)
            if a[n-1][i]==1 and vis[n-1][i]==0:
                dfs(n-1,i)
        c=0
        for i in range(n):
            for j in range(m):
                if a[i][j]==1 and vis[i][j]==0:
                    c+=1
        # print(vis)
        return c
                    
            
        
                
        