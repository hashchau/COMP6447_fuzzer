import csv
import itertools


from .FormatMutator import FormatMutator
from .mutators.StringMutator import StringMutator
from .mutators.FloatMutator import FloatMutator
from .mutators.IntegerMutator import IntegerMutator
import random

class CSVMutator(FormatMutator):

    @staticmethod
    def mutate_once(default_payload, payload):
        mutated_payloads = []
        
        # Create a reader
        csv_reader, spare_csv_reader = itertools.tee(csv.reader(payload.splitlines()))
        if not csv_reader:
            return [default_payload]

        # Create a list of lists 
        csv_list = CSVMutator.convert_csv_to_list(csv_reader)

        rand_num = random.randint(0, 2)
        if rand_num == 0:
            mutated_payloads.append(CSVMutator.convert_list_to_csv(CSVMutator.add_rows(csv_list)))
        elif rand_num == 1:
            mutated_payloads.append(CSVMutator.convert_list_to_csv(CSVMutator.insert_bad_char(csv_list)))
        elif rand_num == 2:
            mutated_payloads.append(CSVMutator.mutate_generic(csv_list))

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
    def add_rows(csv_list, value = "a"):
        num_rows = random.randint(10, 20)
        for i in range(num_rows):
            csv_list = CSVMutator.add_row(csv_list, value)
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
    def insert_bad_char(csv_list):
        mutated_payload = csv_list 
        for row_count, row in enumerate(mutated_payload):
            for col_count, col in enumerate(row):
                try:
                    int(col)
                except ValueError:
                    continue
                mutated_payload[row_count][col_count] = "0"

        return mutated_payload

    @staticmethod
    def mutate_generic(csv_list):
        rand_num = random.randint(0, 2)
        if rand_num == 0:
            return CSVMutator.convert_list_to_csv(CSVMutator.mutate_string(csv_list))
        elif rand_num == 1:
            return CSVMutator.convert_list_to_csv(CSVMutator.mutate_integer(csv_list))
        elif rand_num == 2:
            return CSVMutator.convert_list_to_csv(CSVMutator.mutate_float(csv_list))

    @staticmethod
    def mutate_string(csv_list):
        # Select a random row and column to mutate
        i = random.randint(1, len(csv_list) - 1)
        j = random.randint(0, len(csv_list[0]) - 1)
        
        try:
            if not StringMutator.is_string(csv_list[i][j]):
                return csv_list
        except:
            return csv_list

        rand_num = random.randint(0, 6)
        if rand_num == 0:
            csv_list[i][j] = StringMutator.delete_char(csv_list[i][j])
        elif rand_num == 1:
            csv_list[i][j] = StringMutator.flip_bits(csv_list[i][j])
        elif rand_num == 2:
            csv_list[i][j] = StringMutator.insert_new_line(csv_list[i][j])
        elif rand_num == 3:
            csv_list[i][j] = StringMutator.insert_format_string(csv_list[i][j])
        elif rand_num == 4:
            csv_list[i][j] = StringMutator.extend_string(csv_list[i][j])
        elif rand_num == 5:
            csv_list[i][j] = StringMutator.repeat_string(csv_list[i][j])
        elif rand_num == 6:
            csv_list[i][j] = StringMutator.random_chars(csv_list[i][j])
        
        return csv_list
    
    @staticmethod
    def mutate_integer(csv_list):
        # Select a random row and column to mutate
        i = random.randint(1, len(csv_list) - 1)
        j = random.randint(0, len(csv_list[0]) - 1)
        
        try:
            if not IntegerMutator.is_integer(csv_list[i][j]):
                return csv_list
        except:
            return csv_list
        
        rand_num = random.randint(1,4)
        if rand_num == 0:
            csv_list[i][j] = str(IntegerMutator.add_random(int(csv_list[i][j])))
        elif rand_num == 1:
            csv_list[i][j] = str(IntegerMutator.sub_random(int(csv_list[i][j])))
        elif rand_num == 2:
            csv_list[i][j] = str(IntegerMutator.make_negative(int(csv_list[i][j])))
        elif rand_num == 3:
            csv_list[i][j] = str(IntegerMutator.make_huge(int(csv_list[i][j])))
        elif rand_num == 4:
            csv_list[i][j] = str(IntegerMutator.make_tiny(int(csv_list[i][j])))

        return csv_list

    @staticmethod
    def mutate_float(csv_list):
        # Select a random row and column to mutate
        i = random.randint(1, len(csv_list) - 1)
        j = random.randint(0, len(csv_list[0]) - 1)

        try:
            if not FloatMutator.is_float(csv_list[i][j]):
                return csv_list
        except:
            return csv_list

        rand_num = random.randint(0, 7)
        if rand_num == 0:
            csv_list[i][j] = str(FloatMutator.add_random(float(csv_list[i][j])))
        elif rand_num == 1:
            csv_list[i][j] = str(FloatMutator.sub_random(float(csv_list[i][j])))
        elif rand_num == 2:
            csv_list[i][j] = str(FloatMutator.make_negative(float(csv_list[i][j])))
        elif rand_num == 3:
            csv_list[i][j] = str(FloatMutator.make_huge(float(csv_list[i][j])))
        elif rand_num == 4:
            csv_list[i][j] = str(FloatMutator.make_tiny(float(csv_list[i][j])))
        elif rand_num == 5:
            csv_list[i][j] = str(FloatMutator.make_int(float(csv_list[i][j])))
        elif rand_num == 6: 
            csv_list[i][j] = str(FloatMutator.make_bool(float(csv_list[i][j])))
        elif rand_num == 7:
            csv_list[i][j] = str(FloatMutator.make_null())
        
        return csv_list