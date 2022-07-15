from .Fuzzer import Fuzzer
from .mutators.IntegerMutator import IntegerMutator
import json
from .Harness import Harness
class JSONFuzzer(Fuzzer):
    def __init__(self, binary_path, binary_input_path):
        super().__init__(binary_path, binary_input_path)
        print("Running JSON Fuzzer")
        print(f"binary_path: {self.binary_path}")
        print(f"binary_input_path: {self.binary_input_path}")
        pass

    def fuzz(self):

        proc_ret_code = 0                                
        # Open the input JSON file for reading
        f = open(self.binary_input_path, "r")
        # Create a dictionary from the input JSON file's contents
        input_file_dict = json.load(f)
        # Iterate through the dictionary
        for key, value in input_file_dict.items():
            if isinstance(value, int):
                mutated_value = IntegerMutator.make_huge(value)
                print(f"Mutated value: {mutated_value}")
                mutated_dict = input_file_dict.copy()
                mutated_dict[key] = mutated_value
                print(f"Mutated dictionary: {mutated_dict}")
                mutated_dict_str = json.dumps(mutated_dict)
                mutated_dict_bytes = mutated_dict_str.encode()
                Harness.get_instance().try_payload(mutated_dict_bytes)

        return mutated_dict_str

    def get_coverage():
        return 0.0
    
    def get_type_of_crash():
        return "e.g. buffer overflow"
