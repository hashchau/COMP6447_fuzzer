import csv

from .FormatMutator import FormatMutator
from .mutators.StringMutator import StringMutator


class CSVMutator(FormatMutator):


    # def fuzz(self):
    #     # Open the input JSON file for reading
    #     csv_file = open(self.binary_input_path, "r")
    #     csv_reader = csv.DictReader(csv_file)
    #     num_columns = len(csv_reader.fieldnames) 
    #     print(f"Number of columns: {num_columns}")
    #     mutated_new_line = StringMutator.insert_new_csv_line(num_columns)
    #     print(f"Mutated new line: {mutated_new_line}")
    #     return "blah"

    @staticmethod
    def mutate_once(payload):
        pass
        
        
    @staticmethod
    def mutate_all(payload):
        pass
