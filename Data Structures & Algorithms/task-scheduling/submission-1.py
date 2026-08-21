class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        freq=Counter(tasks)
        heap=[[-count,x] for x,count in freq.items()]
        heapq.heapify(heap)

        cooldown=deque()
        time=0

        while heap or cooldown:
            time+=1

            while cooldown and cooldown[0][2]<=time:
                task,count,cooldowntime=cooldown.popleft()
                heapq.heappush(heap,[-count,task])

            if heap:
                count,task=heapq.heappop(heap)
                count=abs(count)-1
                
                if count>0:
                    cooldown.append([task,count,time+n+1])

        return time
                
        

'''
tc: O(Tlogk) ~ O(T)
sc: O(k)

freq = {'X': 2, 'Y': 2}

heap = [[-2, 'X'], [-2, 'Y']]

cooldown={}

time=1
cooldown is empty
if heap: 
    count=-2 task=X         (heap= [[-2, 'Y']])
    count=abs(count)-1
    cooldown={X,1,4}
    
time=2
check cooldown 4<=2? no
if heap:
    count=-2 task=Y  heap=[]
    count=abs(count)-1=1
    cooldown={(X,1,4)(Y,1,5)}

time=3
check cooldown 4<=3 then check 5<=3 no
heap is empty

time=4
check cooldown 4<=4? yes
    task,count,curr_time=x,1,4  (cooldown={(Y,1,5)})
    push to heap=[[-1,x]]
check cooldown 5<=4? no
if heap? yes
    count=-1 task=X heap=[]
    count=abs(count)-1=0
    dont append to cooldown

time=5
check cooldown 5<=5 yes cooldown={}
    task,count,curr_time=y,1,5
    push to heap=[(-1,y)]
if heap? yes
    count=-1 task=y heap=[]
    count=abs(count)-1=0
    dont append to cooldown

return time=5
------------------------------------------------------------------------------------------------
Input: tasks = ["A","A","A","B","C"], n = 3
freq={A:3, B:1 C:1}
heap=[(-3,A), (-1,B), (-1,C)]
cooldown=[]

initially time=0

time=1
    count,task=-3,A heap=[(-1,B), (-1,C)]
    count=abs(count)-1=2
    cooldown=[[A,2,5]]

time=2
    check cooldown time and currtime-- 5<=2? no
    heap is not empty
        count,task=-1,B heap=[(-1,C)]
        count=abs(1)-1=0
        dont append to cooldown

time=3
    5<=3 no 
    heap is not empty
        count=-1,task=C heap=[]
        count=abs(1)-1=0
        dont append to cooldown

time=4 
    5<=4? no
    heap is empty

time 5
    5<=5? yes 
    task=A, count=2, cooldowntime=5
    append this to heap=[(-2,A)]
    heap is not empty
        count=-2 task=A heap=[]
        count=2-1=1
        cooldown=[[A,1,9]]    

time=6
    9<=6? no 
    heap is empty 

time=7
    9<=7? no
    heap is empty

time=8
    9<=8? no
    heap is empty

time=9
    9<=9 yes
    task,count,time=A,1,9
    count=1-1=0
    dont append to cooldown

A -> B-> C -> idle -> A -> idle -> idle -> idle -> A



'''