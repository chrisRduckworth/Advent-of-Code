## Reverse Engineering
Look at the input. Sometimes it's carefully engineered to make the problem easier - eg graphs are actually just cycles, so you can use LCM to calculate the total cycle length.

Sometimes there aren't good examples. Then make a quick and dirty brute force solution which you can use to compare with your proper solution in tests.

## Algorithms
Memoization/Dynamic processing - for when there's a lot of recalculating in recursion - you can use @cache in python

Queues vs recursion - sometimes (eg with pathfinding), you want to do complete one calculation before moving on to the next, that's when you use a queue.

### Pathfinding
Consider using heapq to make finding the minimum much faster
 - Dijkstra - optimal pathfinding with weighted graphs
 - A* - optimal pathfinding with a heuristic
 - BFS (Breadth-first-search) - general pathfinding, more efficient than basic floodfill
 - D* - Dynamic A\*, for when the graph changes
 - Longest Path - See wikipedia. Hopefully it's a directed acyclic graph, in which case you can use graphlib to sort. If it isn't try to trim the graph by removing nodes which are just straight and turning it into a weighted graph

### Areas
 - Flood fill - for finding what's inside a bounded shape
 - Winding numbers - counting how many times a ray overlaps a border tells you whether it is inside or not
 - Jordan curve - RH along the edge to know if you are inside
 - Region quadtrees? - Essentially splitting a square/rectangle into 4 recursively depending on whether it's inside or outside

## Maths
 - Complex numbers - useful when navigating/rotating
 - Shoelace theorem - for finding area inside a polygon - https://www.themathdoctors.org/polygon-coordinates-and-areas/
 - Pick's Theorem - as above
 - Green's Theorem - as above (apparently? I did vector calculus a long time ago)
 - Chinese Remainder Theorem - calculating cycle lengths or just general modular arithmetic
