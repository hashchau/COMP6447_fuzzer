from .FormatMutator import FormatMutator
from .mutators.StringMutator import StringMutator
from .mutators.IntegerMutator import IntegerMutator
from .mutators.FloatMutator import FloatMutator

import json
import random
class JSONMutator(FormatMutator):

    @staticmethod
    def mutate_once(default_payload, payload):
        input_file_dict = json.loads(payload)
        if not isinstance(input_file_dict, dict):
            return [default_payload]

        rand_num = random.randint(0, 4)
        if rand_num == 0:
            mutated_payload = JSONMutator.mutate_integer(input_file_dict)
        elif rand_num == 1:
            mutated_payload = JSONMutator.mutate_float(input_file_dict)
        elif rand_num == 2:
            mutated_payload = JSONMutator.mutate_string(input_file_dict)
        elif rand_num == 3:
            mutated_payload = JSONMutator.duplicate_dictionaries(input_file_dict, 3)
        elif rand_num == 4:
            mutated_payload = JSONMutator.insert_integer_overflow(default_payload)

        return [json.dumps(mutated_payload)]


    @staticmethod
    def insert_integer_overflow(payload):
        def overflow_integer(value):
            return IntegerMutator.make_huge(value)

        return JSONMutator.apply_function_recursively(payload, overflow_integer)

    @staticmethod
    def insert_integer_underflow(payload):
        def underflow_integer(value):
            return IntegerMutator.make_tiny(value)

        return JSONMutator.apply_function_recursively(payload, underflow_integer)
    
    @staticmethod
    def insert_format_string(payload):
        def format_string(value):
            if StringMutator.is_string(value):
                return StringMutator.insert_format_string(value)

        return JSONMutator.apply_function_recursively(payload, format_string)

    @staticmethod
    def insert_buffer_overflow(payload):
        def overflow_buffer(value):
            if isinstance(value, str):
                return StringMutator.repeat_string(value)

        return JSONMutator.apply_function_recursively(payload, overflow_buffer)


    @staticmethod
    def mutate_integer(payload):
        def mutate_int(value):
            if IntegerMutator.is_integer(value):
                rand_num = random.randint(0, 5)
                if rand_num == 0:
                    return IntegerMutator.bit_flip(value)
                elif rand_num == 1:
                    return IntegerMutator.add_random(value)
                elif rand_num == 2:
                    return IntegerMutator.sub_random(value)
                elif rand_num == 3:
                    return IntegerMutator.make_negative(value)
                elif rand_num == 4:
                    return IntegerMutator.make_huge(value)
                elif rand_num == 5:
                    return IntegerMutator.make_tiny(value)
        return JSONMutator.apply_function_recursively(payload, mutate_int)

    @staticmethod
    def mutate_float(payload):
        def mutate_flt(value):
            if FloatMutator.is_float(value):
                rand_num = random.randint(0, 4)
                if rand_num == 0:
                    return FloatMutator.add_random(float(value))
                elif rand_num == 1:
                    return FloatMutator.sub_random(float(value))
                elif rand_num == 2:
                    return FloatMutator.make_negative(float(value))
                elif rand_num == 3:
                    return FloatMutator.make_huge(float(value))
                elif rand_num == 4:
                    return FloatMutator.make_tiny(float(value))
        return JSONMutator.apply_function_recursively(payload, mutate_flt)

    @staticmethod
    def mutate_string(payload):
        def mutate_str(value):
            if StringMutator.is_string(value):
                rand_num = random.randint(0, 7)
                if rand_num == 0:
                    return StringMutator.delete_char(value)
                elif rand_num == 1:
                    return StringMutator.flip_bits(value)
                elif rand_num == 2:
                    return StringMutator.insert_new_line(value)
                elif rand_num == 3:
                    return StringMutator.insert_format_string(value)
                elif rand_num == 4:
                    return StringMutator.extend_string(value)
                elif rand_num == 5:
                    return StringMutator.repeat_string(value)
                elif rand_num == 6: 
                    return StringMutator.random_chars(value)
                elif rand_num == 7:
                    return StringMutator.make_null()
        return JSONMutator.apply_function_recursively(payload, mutate_str)

    # @staticmethod
    # def insert_bit_overflow(payload):
    #     def overflow_integer(value):
    #         if isinstance(value, int):
    #             return IntegerMutator.make_huge(value)
    #         elif isinstance(value, float):
    #             return FloatMutator.make_huge(value)

    #     return JSONMutator.apply_function_recursively(payload, overflow_integer)

    # @staticmethod
    # def insert_bit_underflow(payload):
    #     def underflow_integer(value):
    #         if isinstance(value, int):
    #             return IntegerMutator.make_tiny(value)
    #         elif isinstance(value, float):
    #             return FloatMutator.make_tiny(value)

    #     return JSONMutator.apply_function_recursively(payload, underflow_integer)
    
    # @staticmethod
    # def insert_format_string(payload):
    #     def format_string(value):
    #         if isinstance(value, str):
    #             return StringMutator.insert_format_string(value)

    #     return JSONMutator.apply_function_recursively(payload, format_string)

    # @staticmethod
    # def insert_buffer_overflow(payload):
    #     def overflow_buffer(value):
    #         if isinstance(value, str):
    #             return StringMutator.repeat_string(value)

    #     return JSONMutator.apply_function_recursively(payload, overflow_buffer)

    @staticmethod
    def duplicate_dictionary(input_file_dict):
        # duplicate the dictionary
        dup_file_dict = {}
        for key, value in input_file_dict.items():
            new_key = key * 2
            dup_file_dict[new_key] = input_file_dict[key]
        mutated_payload = input_file_dict | dup_file_dict
        return mutated_payload

    @staticmethod
    def duplicate_dictionaries(input_file_dict, depth = 1):
        for i in range(depth):
            input_file_dict = JSONMutator.duplicate_dictionary(input_file_dict)
        return input_file_dict

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
