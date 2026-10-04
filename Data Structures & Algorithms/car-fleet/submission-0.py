class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse=True)

        fleet_time = 0
        fleet = 0

        for position, speed in pair:
            time = (target - position) / speed

            if time > fleet_time:
                fleet_time = time
                fleet += 1

        return fleet


"""
tc: O(nlogn)
sc: O(n)

goal - Return the number of different car fleets that will arrive at the destination.

approach: greedy

1. Pair each position with its speed.
2. Sort cars by position descending (closest to target → farthest). The car ahead determines whether the car behind can catch it.
3. Then calculate arrival times in that order.

current_time > fleet_time
→ cannot catch the fleet ahead
→ new fleet

current_time <= fleet_time
→ catches/joins the fleet ahead
→ same fleet

Input: target = 10, position = [1,4], speed = [3,2]

(10-1)/3 = 9/3 = 3 
(10-4)/2 = 6/2 = 3

Both cars take 3 units of time.
The car behind catches the car ahead -> 1 fleet.

-------------------------------------------------------------------------------------------------------

Input: target = 10, position = [4,1,0,7], speed = [2,2,1,1]

[(7, 1), (4, 2), (1, 2), (0, 1)]

(10-7)/1 = 3
(10-4)/2 = 3
(10-1)/2 = 4
(10-0)/1 = 10

3,3,4,10

currenttime>fleettime--> new_fleet
currenttime<=fleettime --> same fleet

fleettime=3 fleet=1
3<=3? same  
4>3? fleettime=4 fleet=2
10>4? yes fleetime =10 fleet=3
"""
