class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:

        outgoing=[0]*(n+1)
        incoming=[0]*(n+1)

        for a, b in trust:
            outgoing[a]+=1
            incoming[b]+=1
        
        for person in range(1,n+1):
            if outgoing[person]==0 and incoming[person]==n-1:
                return person

        return -1    

'''
tc: O(n+t)
sc: O(n)
where t = len(trust)

Input: n = 4, trust = [[1,3],[4,3],[2,3]]
        
          1 2 3 4
incoming  0 0 3 0
outgoing  1 1 0 1

outgoing[person]==0 and incoming[person]==n-1
outgoign[3]==0 and incoming[3]==4-1=3
so ans=3

--------------------------------------------------------
Input: n = 3, trust = [[1,3],[2,3],[3,1],[3,2]]

          1 2 3 
incoming  1 1 2 
outgoing  1 1 2

ans=-1




'''