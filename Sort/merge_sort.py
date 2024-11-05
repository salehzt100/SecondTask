from typing import List
from Services.sort_services import SortServices


class MergeSort:
    def __init__(self, users: List[List[str]], sort_field):
        self.users = users
        self.sort_field_index = SortServices.get_field_index(sort_field) - 1

    def merge(self, left: int, middle: int, right: int):
        left_size = middle - left + 1
        right_size = right - middle
        left_half = [self.users[left + i] for i in range(left_size)]
        right_half = [self.users[middle + 1 + j] for j in range(right_size)]

        i = j = 0
        k = left

        while i < left_size and j < right_size:
            if left_half[i][self.sort_field_index] <= right_half[j][self.sort_field_index]:
                self.users[k] = left_half[i]
                i += 1
            else:
                self.users[k] = right_half[j]
                j += 1
            k += 1

        while i < left_size:
            self.users[k] = left_half[i]
            i += 1
            k += 1

        while j < right_size:
            self.users[k] = right_half[j]
            j += 1
            k += 1

    def merge_sort(self, left: int, right: int):

        if left < right:
            middle = (left + right) // 2
            self.merge_sort(left, middle)
            self.merge_sort(middle + 1, right)
            self.merge(left, middle, right)
