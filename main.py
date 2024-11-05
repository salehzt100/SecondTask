from typing import Union ,List
import asyncio
import time
import sys

from Sort.merge_sort_using_thread import MergeSortUsingThread
from Sort.merge_sort_using_asyncio import MergeSortUsingAsync
from Services.sort_services import SortServices
from Validation.validator import Validator
from Model.user import User


def main():
    num_users: int = 1000000
    file_name: str = 'generated_users.csv'
    sort_field:str = 'first_name'
    sort_order:str = 'asc'
    method:str = 'thread'

    valid = Validator()
    try:
        if '--num-users' in sys.argv:
            num_users = int(sys.argv[sys.argv.index('--num-users') + 1])
            valid.validate(key='num_users', value=num_users)
        if '--file-name' in sys.argv:
            file_name = sys.argv[sys.argv.index('--file-name') + 1]
            valid.validate(key='file_name', value=file_name)
        if '--sort-field' in sys.argv:
            sort_field = sys.argv[sys.argv.index('--sort-field') + 1]
            valid.validate(key='sort_field', value=sort_field)
        if '--sort-order' in sys.argv:
            sort_order = sys.argv[sys.argv.index('--sort-order') + 1]
            valid.validate(key='sort_order', value=sort_order)
        if '--method' in sys.argv:
            method = sys.argv[sys.argv.index('--method') + 1]
            valid.validate(key='method', value=method)

    except Exception as e:
        print(e)
        return

    """ first task """
    # create instance from user class
    model = User(num_users, file_name)

    # start time
    start_time = time.time()

    print('Starting user generation...')

    # add header fields
    model.add_header_fields_to_csv_file()

    # factory create
    model.add_generated_user_with_faker_to_csv_file()

    # end time
    end_time = time.time()
    duration = end_time - start_time


    print(f"Finished generating users and outputting CSV file: {file_name}")
    print(f'Duration for generated users: {duration :.5f} seconds\n')

    """ second task """

    service: SortServices = SortServices()

    users: List[List[str]] = service.return_csv_file_as_list(file_name=file_name)
    merge_sort: Union[MergeSortUsingAsync,MergeSortUsingThread,None] = None
    start_time = time.time()
    print(f'Sorting on {sort_field} with {method}...\n')
    if method == 'thread':
        merge_sort = MergeSortUsingThread(users,sort_field)
        merge_sort.sort()
    elif method == 'asyncio':
        merge_sort = MergeSortUsingAsync(users,sort_field)
        asyncio.run(merge_sort.sort())

    end_time = time.time()
    name_sorted_file=service.insert_sorted_list_to_csv_file(users,sort_field,sort_order)
    print(f'Finished sorting with {method} and outputting CSV file:')
    print(name_sorted_file)
    duration = end_time - start_time
    print(f'Duration: {duration :.5f} seconds\n')


if __name__ == '__main__':
    main()
