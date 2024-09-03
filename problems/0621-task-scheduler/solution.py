import heapq
from collections import deque

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """
        Time Complexity : O( n )
        """
        
        # put highest count task in a queue with idle_time and keep dequeueing when time arrives
        # keep repeating till max_heap or dequeue is empty

        # each task 1 unit t
        result = 0
        task_counts = {}
        for task in tasks:
            if task not in task_counts:
                task_counts[task] = 0
            task_counts[task]-=1

        max_heap = [i for i in task_counts.values()]
        heapq.heapify(max_heap)

        time = 0
        dequeue = deque() # pairs of [-cnt, idle_time]
        while max_heap or dequeue:
            time+=1
            if max_heap:
                # subtract 1, '+' because we are taking negative here
                count = heapq.heappop(max_heap) + 1
                if count:
                    dequeue.append([count, time + n])
            if dequeue and dequeue[0][1] == time:
                heapq.heappush(max_heap, dequeue.popleft()[0])
        return time







        
        
        

        
