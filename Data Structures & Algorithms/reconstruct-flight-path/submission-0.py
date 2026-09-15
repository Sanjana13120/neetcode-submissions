class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = {src:[] for src, dest in tickets}
        for src, dest in sorted(tickets)[::-1]:
            adj[src].append(dest)

        res=[]
        def dfs(src):
            while src in adj and adj[src]:
                dest=adj[src].pop()
                dfs(dest)

            res.append(src)

        dfs('JFK')
        return res[::-1]


"""
tc: O(ElogE)
sc: O(E)


given tickets src and dest

Approach: Hierholzer/postorder DFS

src starts from "JFK"

goal -  reconstruct the flight path that this person took, assuming each ticket was used exactly once.
        in a lexicographically smaller order

Input: tickets = [["BUF","HOU"],["HOU","SEA"],["JFK","BUF"]]

adj[BUF] = HOU
adj[HOU] = SEA
adj[JFK] = BUF

approach: DFS

1. sort the tickets
2. build the adj by reversing. Reversing the sorted tickets lets pop() choose the lexicographically smallest destination first.
3. run the dfs from JFK 
4. if there is no outgoing dest then only append to res else keep running dfs
5. res[::-1] converts the postorder into the itinerary.
src in adj prevents a KeyError for airports that only appear as destinations.

dfs(jfk)   
    adj us BUF
    pop the BUF from adj
    dfs(buf)
        adj is HOU
        pop the HOU from adj
        dfs(HOU)
            adj is SEA
            pop the SEA from adj
            dfs(SEA)
                adj is  []
                res= [SEA]
                return
            hou is []
            res= [SEA HOU]
        buf is []
        res= [SEA HOU BUF]
    jfk is  []
    res= [SEA HOU BUF JFK]

return res[::-1]
["JFK","BUF","HOU","SEA"]
          
------------------------------------------------------------------------------------------------------------

Input: tickets = [["HOU","JFK"],["SEA","JFK"],["JFK","SEA"],["JFK","HOU"]]

adj[HOU]=[JFK]
adj[SEA]=[JFK]
adj[JFK]=[SEA,HOU]

dfs(JFK)
    adj is [SEA,HOU]
        dest=HOU adj[JFK]=[SEA]
            dfs(HOU)
                adj is JFK adj[HOU]=[]
                dfs(JFK)
                    dest = SEA adj[jfk]=[]
                    dfs(SEA)
                        dest=JFK adj[sea]=[]
                        dfs(JFK)
                            adj is []
                            res=[JFK]
                            return
                    sea adj is [] res[JFK,SEA] 
                JFK adj is [] res[JFK,SEA,JFK]      
            HOU adj is [] res[JFK,SEA,JFK,HOU]         
            
    adj of JFK=[]
    res[JFK,SEA,JFK,HOU,JFK]

reverse res
[JFK,HOU,JFK,SEA,JFK]







"""
