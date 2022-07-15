import csv
from .FormatMutator import FormatMutator
from .mutators.StringMutator import StringMutator
class CSVMutator(FormatMutator):

    @staticmethod
    def mutate_once(payload):
        pass
        
    @staticmethod
    def mutate_all(payload):
        mutated_payloads = []
        mutated_payloads.append(payload)
        print(f"payload == {payload}")
        # print(f"num_columns == {num_columns}")
        # mutated_new_line = StringMutator.insert_new_line_with_delimiter("A", ",", num_columns)
        # print(f"mutated_new_line == {mutated_new_line}")
        # mutated_payloads.append(mutated_new_line.encode('utf-8'))
        return mutated_payloads
