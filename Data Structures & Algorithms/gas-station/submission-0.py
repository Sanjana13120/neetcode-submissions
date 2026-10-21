class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        start = 0
        tank = 0

        if sum(gas) < sum(cost):
            return -1

        for i in range(len(gas)):
            tank += gas[i] - cost[i]

            if tank < 0:
                tank = 0
                start = i + 1

        return start


"""
tc: O(n)
sc: O(1)

goal - find the gas station idx so that i can travel around the circuit else -1

Approach: Greedy
1. if sum(gas)<sum(cost)
        return -1
2. Initialize tank = 0 and start = 0.
3. For each index i, calculate netgain = gas[i] - cost[i] and add it to tank
4. if tank<0 start=i+1 and tank=0
5. finally return start 


Input: gas = [1,2,3,4], cost = [2,2,4,1]

gas[3]=4 is the max so i start with start=3 and tank=5

travel 3 to 0:
    cost[3]=1 gas[0]=1
    tank=4-1+1=4

travel 0 to 1:
    cost[0]=2 gas[1]=2
    tank=4-2+2=4

travel 1 to 2:
    cost[1]=2 gas[2]=3
    tank=4-2+3=5

tavel 2 to 3 which is my start idx
    cost[2]=4
    tank=5-4=1>0? so ciruit is complete 

return start=3

tank=0 start=0

sum(gas)=10 
sum(cost)= 9
10>=9 so circuit exists

netgain=gas[i]-cost[i]

i=0 netgain=1-2=-1 newtank= tank+netgain = 0+(-1)=-1 so start=1 tank=0
i=1 netgain=2-2=0  newtank = 0+0=0
i=2 netgain=3-4=-1 newtank = 0+(-1)=-1<0 so start=2 tank=0
i=3 netgain=4-1=3  newtank= 0+3= 3 so tank=3 start=3


-------------------------------------------------------------------------------------------------------------------
Input: gas = [1,2,3], cost = [2,3,2]

6>=7? no
return -1

-------------------------------------------------------------------------------------------------------------------

Input: gas = [1,2,3,4,5], cost = [3,4,5,1,2]
15>=15? yes

tank=0 start=0

i=0 netgain=1-3=-2 newtank=0-2=-2<0 tank=0 start=0
i=1 netgain=2-4=-2 newtank=0-2=-2<0 tank=0 start=0
i=2 netgain=3-5=-2 newtank=0-2=-2<0 tank=0 start=0
i=3 netgain=4-1=3>0  newtank=0+3=3 tank=3 start=3
i=4 netgain=5-2=3>0  newtank=3+3=6 


"""
