import random
from readline import insert_text
from .TypeMutator import TypeMutator

class StringMutator(TypeMutator):
    @staticmethod
    def delete_char(input_string):
        if len(input_string) > 2:
            d = random.randint(0, len(input_string) - 1)
            return input_string[:d] + input_string[d + 1:]

        return input_string
    
    @staticmethod
    def flip_bits(input_string):
        byte_array_of_chars = bytearray(input_string, 'utf-8')
        try:
            flip_location = random.randint(0, len(byte_array_of_chars) - 1)
            byte_array_of_chars[flip_location] ^= 0xF
            return byte_array_of_chars.decode()
        except ValueError:
            return input_string


    @staticmethod
    def insert_new_line(input_string):
        try:
            replacement_location = random.randint(0, len(input_string) - 1)
            input_string = input_string[:replacement_location] + '\n' + input_string[replacement_location:]
        except:
            pass
        return input_string
    
    @staticmethod
    def insert_new_line_with_delimiter(char, delimiter, num_columns):
        mutated_string_component = char + delimiter
        mutated_string = mutated_string_component * (num_columns - 1) + char
        return mutated_string

    @staticmethod
    def insert_format_string(input_string):
        if (len(input_string) - 1) > 0:
            format_chars = ['%s', '%n', '%x', '%p']
        
            mutated_string = input_string
        
            replacement_location = random.randint(0, len(input_string) - 1)
            replacement_character = random.choice(format_chars)
            mutated_string = mutated_string[:replacement_location] + replacement_character + mutated_string[replacement_location:]
        
            return mutated_string

        return input_string

    @staticmethod
    def extend_string(input_string):
        extend_size = random.randint(0, 5)
        mutated_string = input_string + ('A'*extend_size)
        return mutated_string

    @staticmethod
    def repeat_string(input_string):
        repeats = random.randint(0, 5)
        mutated_string = input_string
        mutated_string = mutated_string*repeats
        return mutated_string

    @staticmethod
    def random_chars(input_string):
        if (len(input_string) - 1) > 0:
            mutated_string = input_string
    
            replacement_location = random.randint(0, len(input_string) - 1)
            replacement_character = chr(random.randint(0, 255))
            
            if replacement_character != '\n':
                mutated_string = mutated_string[:replacement_location] + replacement_character + mutated_string[replacement_location + 1:]
        
            return mutated_string

        return input_string
    
    @staticmethod
    def make_null():
        return None
    
    @staticmethod
    def is_string(input_string):
        if not isinstance(input_string, str):
            return False

        return not input_string.lstrip("-").isdigit()
