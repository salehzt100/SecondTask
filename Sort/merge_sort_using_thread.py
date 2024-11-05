from threading import Thread
from typing import List
from Sort.merge_sort import MergeSort


class MergeSortUsingThread(MergeSort):

    def __init__(self, users: List[List[str]], sort_field):
        super().__init__(users, sort_field)



    def sort_partition(self, left: int, right: int):
        self.merge_sort(left, right)

    def thread_sort(self):
        left = 0
        right = len(self.users) - 1
        middle = (left + right) // 2

        th1 = Thread(target=self.sort_partition, args=(left, middle), name='thread-1')
        th2 = Thread(target=self.sort_partition, args=(middle + 1, right), name='thread-2')
        th1.start()
        th2.start()
        th1.join()
        th2.join()

        self.merge(left, middle, right)

    def sort(self):
        self.thread_sort()
