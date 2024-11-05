class BasicRulesValidation:
    def __init__(self):
        pass

    @staticmethod
    def validate_rule_is_string(key: str, value: str) -> bool:
        if not isinstance(value, str):
            raise TypeError(f"Exception: Value for '{key}' must be a string.")
        return True

    @staticmethod
    def validate_rule_is_integer(key: str, value: int) -> bool:
        if not isinstance(value, int):
            raise TypeError(f"Exception: Value for '{key}' must be an integer.")
        return True

    @staticmethod
    def validate_rule_is_exist_in_sort_type(key: str, value: str) -> bool:
        valid_sort_types = ['asc', 'desc']
        if value not in valid_sort_types:
            raise ValueError(f"Exception: Invalid sort type '{value}' for '{key}'. Expected one of {valid_sort_types}.")
        return True

    @staticmethod
    def validate_rule_is_more_than_zero(key: str, value: int) -> bool:
        if value <= 0:
            raise ValueError(f"Exception: Value for '{key}' must be greater than zero.")
        return True

    @staticmethod
    def validate_rule_is_file_extension(key: str, value: str) -> bool:
        if not value.endswith('.csv'):
            raise ValueError(f"Exception: The file name '{value}' for '{key}' must have a .csv extension.")
        return True

    @staticmethod
    def validate_rule_is_exist_in_user_data(key: str, value: str) -> bool:
        valid_user_fields = [
            'user_id', 'first_name', 'last_name', 'email',
            'phone_number', 'date_of_birth', 'address',
            'city', 'state', 'country', 'zip_code',
            'username', 'password', 'account_created', 'is_active'
        ]
        if value not in valid_user_fields:
            raise ValueError(f"Exception: '{value}' is not a valid field in user data for '{key}'."
                             f" Valid fields are: {', '.join(valid_user_fields)}.")
        return True

    @staticmethod
    def validate_rule_is_exist_in_method_type(key: str, value: str) -> bool:
        valid_method_types = ['thread', 'asyncio']
        if value not in valid_method_types:
            raise ValueError(f"Exception: '{value}' is not a valid method type for '{key}'. "
                             f"Valid method types are: {', '.join(valid_method_types)}.")
        return True
