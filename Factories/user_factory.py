from faker import Faker
from typing import Generator, List, Union
from datetime import date

class UserFactory:

    def __init__(self, num_users: int) -> None:
        self.num_users = num_users


    def create_user_with_fake_data(self) -> Generator:
        """
             generate row of fake data by faker module, and yield each row to addGeneratedUserWithFakerToCsvFile() method
              to store it in csv file
        """

        fake: Faker = Faker()
        for i in range(self.num_users):
            row :List[Union[str, int, date, bool ]] = [
                i + 1,    #unique
                fake.first_name(),
                fake.last_name(),
                fake.unique.email(),   #unique
                fake.unique.phone_number(),  #unique
                fake.date_of_birth(),
                fake.address(),
                fake.city(),
                fake.state(),
                fake.country(),
                fake.zipcode(),
                fake.unique.user_name(),    #unique
                fake.password(),
                fake.past_date(),
                fake.boolean()
            ]
            yield row


