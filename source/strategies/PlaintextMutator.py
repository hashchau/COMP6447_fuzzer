from .FormatMutator import FormatMutator
from .mutators.StringMutator import StringMutator
from .mutators.IntegerMutator import IntegerMutator

import json
import random

class PlaintextMutator(FormatMutator):

    @staticmethod
    def mutate_once(payload):
        mutated_payload = PlaintextMutator.mutate_string(payload)

        return [mutated_payload]

    @staticmethod
    def mutate_all(payload):
        mutated_payload = PlaintextMutator.mutate_string(payload)

        return [mutated_payload]

    @staticmethod
    def mutate_string(payload):
        num_mutations = random.randint(1,10)
        mutated_string = payload

        for i in range(num_mutations):
            mutation = random.randint(0,7)

            if mutation == 0:
                mutated_string = StringMutator.delete_char(mutated_string)
            elif mutation == 1:
                mutated_string = StringMutator.flip_bit(mutated_string)
            elif mutation == 2:
                mutated_string = StringMutator.insert_new_line(mutated_string)
            elif mutation == 3:
                mutated_string = StringMutator.insert_new_line_with_delimiter(mutated_string)
            elif mutation == 4:
                mutated_string = StringMutator.insert_format_string(mutated_string)
            elif mutation == 5:
                mutated_string = StringMutator.extend_string(mutated_string)
            elif mutation == 6:
                mutated_string = StringMutator.repeat_string(mutated_string)
            elif mutation == 7:
                mutated_string = StringMutator.random_chars(mutated_string)
            

        return mutated_string

    @staticmethod
    def mutate_integer(payload):

        return mutated_integer