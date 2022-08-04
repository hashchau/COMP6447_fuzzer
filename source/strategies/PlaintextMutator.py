from .FormatMutator import FormatMutator
from .mutators.StringMutator import StringMutator
from .mutators.IntegerMutator import IntegerMutator

import json
import random

class PlaintextMutator(FormatMutator):

    @staticmethod
    def mutate_once(payload):
        inputs = payload.split('\n')[:-1]

        # Choose random line for fuzzing
        fuzz_line = random.randint(0, len(inputs))
        
        if inputs[fuzz_line].isdigit():
            inputs[fuzz_line] = PlaintextMutator.mutate_integer(inputs[fuzz_line])
        else:
            inputs[fuzz_line] = PlaintextMutator.mutate_string(inputs[fuzz_line])
        
        mutated_payload = '\n'.join(inputs) + '\n'
        
        return [mutated_payload]

    @staticmethod
    def mutate_all(payload):
        return PlaintextMutator.mutate_once(payload)

    @staticmethod
    def mutate_string(payload):
        mutated_string = payload
        
        mutation = random.randint(0,4)

        if mutation == 0:
            mutated_string = StringMutator.delete_char(mutated_string)
        elif mutation == 1:
            mutated_string = StringMutator.insert_format_string(mutated_string)
        elif mutation == 2:
            mutated_string = StringMutator.extend_string(mutated_string)
        elif mutation == 3:
            mutated_string = StringMutator.repeat_string(mutated_string)
        elif mutation == 4:
            mutated_string = StringMutator.random_chars(mutated_string)
            
        return mutated_string

    @staticmethod
    def mutate_integer(payload):
        mutation = random.randint(0,8)
        mutated_integer = 0

        if mutation == 0:
            mutated_integer = IntegerMutator.bit_flip(int(payload))
        elif mutation == 1:
            mutated_integer = IntegerMutator.add_random(int(payload))
        elif mutation == 2:
            mutated_integer = IntegerMutator.sub_random(int(payload))
        elif mutation == 3:
            mutated_integer = IntegerMutator.make_negative(int(payload))
        elif mutation == 4:
            mutated_integer = IntegerMutator.make_huge(int(payload))
        elif mutation == 5:
            mutated_integer = IntegerMutator.make_tiny(int(payload))
        elif mutation == 6:
            mutated_integer = IntegerMutator.make_float(int(payload))
        elif mutation == 7:
            mutated_integer = IntegerMutator.make_bool(int(payload))
        elif mutation == 8:
            mutated_integer = IntegerMutator.make_null(int(payload))

        return str(mutated_integer)
