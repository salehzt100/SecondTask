import asyncio
from typing import List
from Sort.merge_sort import MergeSort


class MergeSortUsingAsync(MergeSort):
    def __init__(self, users: List[List[str]],sort_field):
        super().__init__(users, sort_field)

    async def sort_partition(self, left: int, right: int):

        await asyncio.to_thread(self.merge_sort, left, right)


    async def async_sort(self, left: int, right: int):

        if left < right:
            middle = (left + right) // 2
            task1 = asyncio.create_task(self.sort_partition(left, middle))
            task2 = asyncio.create_task(self.sort_partition(middle + 1, right))
            await asyncio.gather(task1, task2)

            self.merge(left, middle, right)

    async def sort(self):
        await self.async_sort(0, len(self.users) - 1)
