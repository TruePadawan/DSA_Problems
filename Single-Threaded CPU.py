from typing import List

"""
I need a min-heap where each node is a 2-tuple (lowest processing time, index)
Loop through the task list, for each task:
    If its enqueue time is <= current time:
        add it to the heap

Process any current task

If CPU is idle:
    pick the next task

return processing order
"""
import heapq


class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        order = []
        enqueue_heap = []
        available_tasks = []

        for i in range(len(tasks)):
            enqueue_time, processing_time = tasks[i]
            heapq.heappush(enqueue_heap, (enqueue_time, i))
        first_task = enqueue_heap[0]
        current_time = first_task[0]

        while len(order) < len(tasks):
            while len(enqueue_heap) > 0 and enqueue_heap[0][0] <= current_time:
                task = heapq.heappop(enqueue_heap)
                task_index = task[1]
                task_processing_time = tasks[task_index][1]
                heapq.heappush(available_tasks, (task_processing_time, task_index))
            if len(available_tasks) > 0:
                processing_time, index = heapq.heappop(available_tasks)
                current_time += processing_time
                order.append(index)
            else:
                next_task = enqueue_heap[0]
                current_time = next_task[0]

        return order


soln = Solution()
print(soln.getOrder(
    [[1, 2], [2, 4], [3, 2], [4, 1]]))
