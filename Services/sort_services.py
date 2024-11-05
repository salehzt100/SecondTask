import csv
from typing import List
from Model.user import User


class SortServices:

    fieldsDic : dict[str, int] = {
        'user_id': 1,
        'first_name': 2,
        'last_name': 3,
        'email': 4,  # unique
        'phone_number': 5,  # unique
        'date_of_birth': 6,
        'address': 7,
        'city': 8,
        'state': 9,
        'country': 10,
        'zip_code': 11,
        'username': 12,  # unique
        'password': 13,
        'account_created': 14,
    }

    @staticmethod
    def return_csv_file_as_list(file_name: str) -> List[List[str]]:
        with open(f'{file_name}', 'r') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            next(reader)   # to skip the header row
            return list(reader)

    @staticmethod
    def insert_sorted_list_to_csv_file(users:List[List[str]], sort_field: str, sort_order: str) -> str:
        new_file_name=f'generated_users_sorted_by_{sort_field}_{sort_order}.csv'
        model = User(file_name=new_file_name)
        model.add_header_fields_to_csv_file()
        with open(new_file_name, 'a') as csvfile:
            writer = csv.writer(csvfile)
            if sort_order == 'asc':
                writer.writerows(users)
            elif sort_order == 'desc':
                writer.writerows(reversed(users))
        return new_file_name


    @staticmethod
    def get_field_index(field_name: str) -> int:
        return SortServices.fieldsDic.get(field_name, -1)
