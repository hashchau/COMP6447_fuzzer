from .FormatMutator import FormatMutator
from .mutators.StringMutator import StringMutator
from .mutators.IntegerMutator import IntegerMutator

import json
import random
class JSONMutator(FormatMutator):

    @staticmethod
    def mutate_once(default_payload, payload):
        input_file_dict = json.loads(payload)

        rand_num = random.randint(0,3)
        if rand_num == 0:
            mutated_payload = JSONMutator.insert_integer_overflow(input_file_dict)
        elif rand_num == 1:
            mutated_payload = JSONMutator.insert_integer_underflow(input_file_dict)
        elif rand_num == 2:
            pass
        elif rand_num == 3:
            mutated_payload = JSONMutator.insert_format_string(input_file_dict)
        elif rand_num == 4:
            pass
        return [json.dumps(mutated_payload)]

    @staticmethod
    def insert_integer_overflow(payload):
        def overflow_integer(value):
            if isinstance(value, int):
                return IntegerMutator.make_huge(value)

        return JSONMutator.apply_function_recursively(payload, overflow_integer)

    @staticmethod
    def insert_integer_underflow(payload):
        def underflow_integer(value):
            if isinstance(value, int):
                return IntegerMutator.make_tiny(value)

        return JSONMutator.apply_function_recursively(payload, underflow_integer)
    
    @staticmethod
    def insert_format_string(payload):
        def format_string(value):
            if isinstance(value, str):
                return StringMutator.insert_format_string(value)

        return JSONMutator.apply_function_recursively(payload, format_string)

    @staticmethod
    def insert_buffer_overflow(payload):
        def overflow_buffer(value):
            if isinstance(value, str):
                return StringMutator.repeat_string(value)

        return JSONMutator.apply_function_recursively(payload, overflow_buffer)

    @staticmethod
    def apply_function_recursively(obj, func):
        if obj is None:
            return None

        if not isinstance(obj, list) and not isinstance(obj, dict):
            return func(obj)
        
        if isinstance(obj, dict):
            for key, value in obj.items():
                obj[key] = JSONMutator.apply_function_recursively(value, func)
        
        if isinstance(obj, list):
            for i, value in enumerate(obj):
                obj[i] = JSONMutator.apply_function_recursively(value, func)

        return obj

    @staticmethod
    def duplicate_dictionary(input_file_dict):
        # duplicate the dictionary
        dup_file_dict = {}
        for key, value in input_file_dict.items():
            new_key = key * 2
            dup_file_dict[new_key] = input_file_dict[key]
        mutated_payload = input_file_dict | dup_file_dict
