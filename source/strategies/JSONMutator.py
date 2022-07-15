from .FormatMutator import FormatMutator
from .mutators.IntegerMutator import IntegerMutator
import json
class JSONMutator(FormatMutator):

    @staticmethod
    def mutate_once(payload):
        pass
        
    @staticmethod
    def mutate_all(payload):
        mutated_payloads = []
        input_file_dict = JSONMutator.bytes_to_json(payload)
        # Iterate through the dictionary
        for key, value in input_file_dict.items():
            if isinstance(value, int):
                mutated_value = IntegerMutator.make_huge(value)
                # print(f"Mutated value: {mutated_value}")
                mutated_dict = input_file_dict.copy()
                mutated_dict[key] = mutated_value
                print(f"Mutated dictionary: {mutated_dict}")
                mutated_dict_str = json.dumps(mutated_dict)
                mutated_dict_bytes = mutated_dict_str.encode()
                mutated_payloads.append(mutated_dict_bytes)

        return mutated_payloads
        
    @staticmethod
    def bytes_to_json(payload):
        json_data = payload.decode("utf-8")
        return json.loads(json_data)
    	
    @staticmethod
    def json_to_bytes(payload):
        json.dumps(payload).encode('utf-8')