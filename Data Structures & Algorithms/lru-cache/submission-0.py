class Node:
    def __init__(self,key,val):
        self.key=key
        self.val=val
        self.prev=None
        self.next=None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.cache={}

        self.head=Node(0,0)
        self.tail=Node(0,0)
        self.head.next=self.tail
        self.tail.prev=self.head

    def add(self,node):
        prev=self.tail.prev
        nxt=self.tail

        prev.next=nxt.prev=node
        node.prev=prev
        node.next=nxt
    
    def remove(self,node):
        prev=node.prev 
        nxt=node.next 

        prev.next=nxt
        nxt.prev=prev
        

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.add(self.cache[key])
            return self.cache[key].val
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        
        self.cache[key]=Node(key,value)
        self.add(self.cache[key])

        if len(self.cache)>self.capacity:
            lru=self.head.next
            self.remove(lru)
            del self.cache[lru.key]

        
'''
tc: O(1)
sc: O(n)

we will use  HashMap → quickly finds the node   (key → node)
Doubly Linked List → maintains LRU → MRU order (HEAD ↔ ... ↔ TAIL)

Node has: key, val, prev, next

LRU cache has:  capacity, hashmap and head <=> tail 

add(self,A) say u have head <=> tail  and now add A

prev=self.tail.prev --head
nxt=self.tail --tail

prev.next=nxt.prev=node
node.prev=prev
node.next=nxt

head <=> A <=> tail 

remove(self,node)
head <=> A <=> tail  remove A

prev=node.prev (head)
nxt=node.next (tail)

prev.next=nxt
nxt.prev=prev

head <=> tail

case 1: put(B,99)
head <=> A <==> B<==> C <=> tail 
check if B is in cache? yes 
    remove it  head <=> A <==> C <=> tail 
now create node B and add 
head <=> A <==> C <==> B<=> tail 

case 2: put(D,9) -- head <=> A <==> B<==> C <=> tail 
check if D is in cache? no
create node D and add
head <=> A <==> B<==> C <==> D <=> tail but capacity=3

len(cache)>cap?
lru=self.head.next = A
so remove this A
del A from cache



'''