import csv
import itertools
from io import StringIO
from .FormatMutator import FormatMutator
from .mutators.StringMutator import StringMutator
import random
import copy

class CSVMutator(FormatMutator):

    @staticmethod
    def mutate_once(default_payload, payload):
        mutated_payloads = []
        
        # Create a reader
        csv_reader, spare_csv_reader = itertools.tee(csv.reader(payload.splitlines()))
        # Create a list of lists 
        csv_list = CSVMutator.convert_csv_to_list(csv_reader)
        rand_num = random.randint(0,1)
        if rand_num == 0:
            # Add multiple rows to the payload
            mutated_payloads.append(CSVMutator.convert_list_to_csv(CSVMutator.add_row(csv_list)))
             
        elif rand_num == 1:
            # mutated_payload = copy.deepcopy(csv_list)
            mutated_payload = csv_list 
            for row_count, row in enumerate(mutated_payload):
                for col_count, col in enumerate(row):
                    try:
                        int(col)
                    except ValueError:
                        continue
                    mutated_payload[row_count][col_count] = "0"
            mutated_payloads.append(CSVMutator.convert_list_to_csv(mutated_payload))
        return mutated_payloads

    @staticmethod
    def generate_list(value, num_columns):
        new_string = value * num_columns
        return list(new_string)

    @staticmethod
    def add_row(csv_list, value = "a"):
        list_of_char = CSVMutator.generate_list(value, len(csv_list[0]))
        csv_list.append(list_of_char)
        return csv_list

    @staticmethod
    def add_column(csv_list, value = "A"):
        for row in csv_list:
            row.append(value)
        return csv_list    

    @staticmethod
    def convert_list_to_csv(list_of_lists):
        new_list = []
        for row in list_of_lists:
            new_row = ",".join(row)
            new_list.append(new_row)
        mutated_payload = "\n".join(new_list)
        return mutated_payload

    @staticmethod
    def convert_csv_to_list(csv_reader):
        # Create a list of lists 
        csv_list = []
        for row in csv_reader:
            csv_list.append(row)
        
        return csv_list

    @staticmethod
    def remove_row(csv_list, row_num):
        pass

    @staticmethod
    def remove_column(csv_list, column_num):
        pass

    @staticmethod
    def replace_str_with_format_str(csv_list):
        pass