import csv
import itertools
from io import StringIO
from .FormatMutator import FormatMutator
from .mutators.StringMutator import StringMutator
class CSVMutator(FormatMutator):

    @staticmethod
    def mutate_once(payload):
        pass
        
    @staticmethod
    def mutate_all(payload):
        mutated_payloads = []
        # print(f"split payload: {payload.splitlines()}")
        csv_reader, csv_reader_spare = itertools.tee(csv.reader(payload.splitlines()))

        # Count number of columns in the csv file
        num_columns = len(next(csv_reader_spare))        
        del csv_reader_spare
        # Create a list of lists 
        csv_list = []
        for row in csv_reader:
            csv_list.append(row)


        new_list = CSVMutator.get_list_of_chars(num_columns, "A")
        
        csv_list.append(new_list)
        # print(f"csv_list before == {csv_list}")
        new_list = []
        for row in csv_list:
            new_row = ",".join(row)
            # print(f"row == {row}")
            new_list.append(new_row)
        # print(f"new_list == {new_list}")

        mutated_payload = "\n".join(new_list)
        # print(f"mutated_payload == {mutated_payload}")

        # file = StringIO()
        # csv.writer(file).writerow(csv_list)

        # print(payload)
        
        # print(file.getvalue())

        mutated_payloads.append(mutated_payload)
        return mutated_payloads
    
    
    @staticmethod
    def get_list_of_chars(num_columns, char):
        new_string = char * num_columns
        return list(new_string)

    @staticmethod
    def add_row(payload, row):
        list_of_char = get_list_of_chars(len(row), "A")
        row.append(list_of_char)
        return row

    @staticmethod
    def add_columns():
        pass
    
    @staticmethod
    def convert_list_to_csv(list_of_lists):

        pass
