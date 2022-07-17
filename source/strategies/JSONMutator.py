from .FormatMutator import FormatMutator
from .mutators.IntegerMutator import IntegerMutator
import json
import random
class JSONMutator(FormatMutator):

    @staticmethod
    def mutate_once(payload):
        # mutated_payloads = []
        # input_file_dict = json.loads(payload)
        return JSONMutator.mutate_all(payload)
        
    @staticmethod
    def mutate_all(payload):
        mutated_payloads = []
        input_file_dict = json.loads(payload)
        # Iterate through the dictionary
        for key, value in input_file_dict.items():
            if isinstance(value, int):
                
                mutated_value = IntegerMutator.make_huge(value)
                # print(f"Mutated value: {mutated_value}")
                mutated_dict = input_file_dict.copy()
                mutated_dict[key] = mutated_value
                mutated_dict_str = json.dumps(mutated_dict)
                mutated_dict_bytes = mutated_dict_str
                mutated_payloads.append(mutated_dict_bytes)

        return mutated_payloads
    
