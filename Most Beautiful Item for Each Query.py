from typing import List


class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        answer = [0] * len(queries)
        real_queries = []
        for index, query in enumerate(queries):
            real_queries.append([query, index])
        real_queries.sort(key=lambda x: x[0])
        items.sort(key=lambda x: x[0])
        max_beauty = 0
        items_pointer = 0
        for query_data in real_queries:
            query, index = query_data
            for i in range(items_pointer, len(items)):
                if items[i][0] <= query:
                    max_beauty = max(max_beauty, items[i][1])
                else:
                    break
                items_pointer = i
            answer[index] = max_beauty
        return answer
