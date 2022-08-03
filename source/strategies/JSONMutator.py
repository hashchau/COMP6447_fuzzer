from .FormatMutator import FormatMutator
from .mutators.StringMutator import StringMutator
from .mutators.IntegerMutator import IntegerMutator

import json
import random
class JSONMutator(FormatMutator):

    @staticmethod
    def mutate_once(payload):
        input_file_dict = json.loads(payload)

        rand_num = random.randint(0,2)
        print(f"trying strategy {rand_num}")
        if rand_num == 0:
            mutated_payload = JSONMutator.insert_integer_overflow(input_file_dict)
        elif rand_num == 1:
            mutated_payload = JSONMutator.insert_integer_underflow(input_file_dict)
        elif rand_num == 2:
            # duplicate the dictionary
            dup_file_dict = {} 
            print(f"dup_file_dict: \n{dup_file_dict}")
            for key, value in input_file_dict.items():
                new_key = key * 2
                dup_file_dict[new_key] = input_file_dict[key]
            mutated_payload = input_file_dict | dup_file_dict
        print(f"mutated payload: \n{mutated_payload}")
        return [json.dumps(mutated_payload)]

    @staticmethod
    def mutate_all(payload):
        input_file_dict = json.loads(payload)
        mutated_payloads = []

        mutated_payloads.append(JSONMutator.insert_integer_overflow(input_file_dict))
        mutated_payloads.append(JSONMutator.insert_integer_underflow(input_file_dict))

        return json.dumps(mutated_payloads)

    

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
