import random
from readline import insert_text
from .TypeMutator import TypeMutator

class StringMutator(TypeMutator):
    
    @staticmethod
    def mutate(input_string):
        pass

    @staticmethod
    def delete_char(input_string):
        if len(input_string) > 2:
            d = random.randint(0, len(input_string) - 1)
            return input_string[:d] + input_string[d + 1:]

        return input_string
    
    @staticmethod
    def flip_bit(input_string):
        chars = bytearray(str(input_string), 'utf-8')
        flip_location = random.randint(0, len(chars) - 1)
        chars[flip_location] ^= 0xFF
        return str(chars)

    @staticmethod
    def insert_new_line(input_string):
        replacement_location = random.randint(0, len(input_string) - 1)
        mutated_string = input_string[:replacement_location] + '\n' + input_string[replacement_location:]
        return mutated_string
    
    @staticmethod
    def insert_new_line_with_delimiter(char, delimiter, num_columns):
        mutated_string_component = char + delimiter
        mutated_string = mutated_string_component * (num_columns - 1) + char
        return mutated_string

    @staticmethod
    def insert_format_string(input_string):
        if (len(input_string) - 1) > 0:
            format_chars = ['%s', '%n', '%x', '%p']
        
            num_replacements = random.randint(0, len(input_string) - 1)
            mutated_string = input_string
        
            for i in range(0, num_replacements):
                replacement_location = random.randint(0, len(input_string) - 1)
                replacement_character = random.choice(format_chars)
                mutated_string = mutated_string[:replacement_location] + replacement_character + mutated_string[replacement_location:]
        
            return mutated_string

        return input_string

    @staticmethod
    def extend_string(input_string):
        extend_size = random.randint(0, 100)
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
            num_replacements = random.randint(0, len(input_string) - 1)
            mutated_string = input_string
            for i in range(0, num_replacements):
                replacement_location = random.randint(0, len(input_string) - 1)
                replacement_character = chr(random.randint(0, 255))
            
                if replacement_character != '\n':
                    mutated_string = mutated_string[:replacement_location] + replacement_character + mutated_string[replacement_location + 1:]
        
            return mutated_string

        return input_string
    
