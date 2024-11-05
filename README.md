# SecondTask

## Objective
This project extends the existing user data generation script to include sorting capabilities for the generated CSV file. Users can sort the data by a specified field using either thread-based or asyncio-based approaches.

## Requirements

### Sorting Options
- Allow the user to specify a field for sorting the CSV file (e.g., `user_id`, `first_name`, `date_of_birth`, etc.).
- Provide options for both ascending and descending sorting.

### Concurrent Sorting Implementations
- Implement two separate functions to handle sorting:
  - **Thread-based sorting**: Utilize Python’s threading module for concurrent sorting.
  - **Asyncio-based sorting**: Utilize asyncio for asynchronous sorting.

### Command-Line Interface (CLI)
- Update the script's CLI to allow users to:
  - Specify the sorting field.
  - Choose sorting order (asc for ascending or desc for descending).
  - Specify the concurrency method (thread or asyncio).
  - Specify the number of users to generate.

### Logging
- Log the start and end time for each sorting method.
- Calculate and display the duration of the sorting process for comparison between thread-based and asyncio-based sorting.

### Sorting Process
- Read the generated CSV file, sort the data based on the specified field and order, and write the sorted data back to a new file.

## Default Values
- `num_users: int = 1000000`
- `file_name: str = 'generated_users.csv'`
- `sort_field: str = 'first_name'`
- `sort_order: str = 'asc'`
- `method: str = 'thread'`

## Example Usage
To sort by `first_name` using threads in ascending order:
```bash
python main.py --num-users 1000 --sort-field first_name --sort-order asc --method thread
```


## Test With Asyncio

<img width="879" alt="Screenshot 2024-11-05 at 4 24 58 PM" src="https://github.com/user-attachments/assets/edd82254-0238-4565-9446-b903d34f6b6d">

## Test With Thread

<img width="670" alt="Screenshot 2024-11-05 at 4 23 54 PM" src="https://github.com/user-attachments/assets/3d555f01-05e0-438d-9c32-adf77f7f9053">

## creat and sort 100 user

<img width="720" alt="Screenshot 2024-11-05 at 4 19 06 PM" src="https://github.com/user-attachments/assets/547dc751-5864-4b33-b2a3-a73018752e00">
