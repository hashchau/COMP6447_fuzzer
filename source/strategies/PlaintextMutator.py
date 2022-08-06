from .FormatMutator import FormatMutator
from .mutators.StringMutator import StringMutator
from .mutators.IntegerMutator import IntegerMutator
from .mutators.FloatMutator import FloatMutator

import random

class PlaintextMutator(FormatMutator):

    @staticmethod
    def mutate_once(default_payload, payload):
        inputs = payload.split('\n')[:-1]

        # Choose random line of payload for fuzzing
        fuzz_line = random.randint(0, (len(inputs) - 1))
        
        if inputs[fuzz_line].lstrip("-").isdigit():
            inputs[fuzz_line] = PlaintextMutator.mutate_integer(inputs[fuzz_line])
        else:
            inputs[fuzz_line] = PlaintextMutator.mutate_string(inputs[fuzz_line])
        
        mutated_payload = '\n'.join(inputs) + '\n'
        
        default_inputs = default_payload.split('\n')[:-1]

        if IntegerMutator.is_integer(default_inputs[fuzz_line]):
            default_inputs[fuzz_line] = PlaintextMutator.mutate_integer(default_inputs[fuzz_line])
        elif FloatMutator.is_float(default_inputs[fuzz_line]):
            default_inputs[fuzz_line] = PlaintextMutator.mutate_float(default_inputs[fuzz_line])
        else:
            default_inputs[fuzz_line] = PlaintextMutator.mutate_string(default_inputs[fuzz_line])

        mutated_default_payload = '\n'.join(default_inputs) + '\n'

        return [mutated_payload, mutated_default_payload]

    @staticmethod
    def mutate_string(payload):
        mutated_string = payload
        
        mutation = random.randint(0,5)

        if mutation == 0:
            mutated_string = StringMutator.delete_char(mutated_string)
        elif mutation == 1:
            mutated_string = StringMutator.insert_format_string(mutated_string)
        elif mutation == 2:
            mutated_string = StringMutator.extend_string(mutated_string)
        elif mutation == 3:
            mutated_string = StringMutator.random_chars(mutated_string)
        elif mutation == 4:
            mutated_string = StringMutator.repeat_string(mutated_string)
        elif mutation == 5:
            mutated_string = StringMutator.flip_bits(mutated_string)
            
        return mutated_string

    @staticmethod
    def mutate_integer(payload):
        mutation = random.randint(0,5)
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

        return str(mutated_integer)

    @staticmethod
    def mutate_float(payload):
        mutation = random.randint(0,4)

        if mutation == 0:
            mutated_float = FloatMutator.add_random(float(payload))
        elif mutation == 1:
            mutated_float = FloatMutator.sub_random(float(payload))
        elif mutation == 2:
            mutated_float = FloatMutator.make_negative(float(payload))
        elif mutation == 3:
            mutated_float = FloatMutator.make_huge(float(payload))
        elif mutation == 4:
            mutated_float = FloatMutator.make_tiny(float(payload))

        return str(mutated_float)