from typing import Union
from Validation.basic_rules_validation import BasicRulesValidation

class Validator:
    def __init__(self):
        self.validation_rules={
            'num_users':['integer','mor_than_zero',],
            'file_name':['string','file_extension'],
            'sort_field':['string','exist_in_user_data'],
            'sort_order':['string','exist_in_sort_type'],
            'method':['string','exist_in_method_type'],
        }

    def validate(self, key: str, value: Union[str, int ,None]):
        rules = self.validation_rules[key]

        for rule in rules:
            method_name = 'validate_rule_is_' + rule

            method = getattr(BasicRulesValidation, method_name, None)
            if method:
                method(key,value)

