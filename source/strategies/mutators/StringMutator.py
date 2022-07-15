import random
from TypeMutator import TypeMutator

class StringMutator(TypeMutator):
    def __init__(self):
        pass
    
    @staticmethod
    def mutate(input_string):
        pass

    
    @staticmethod
    def flip_bit(input_string):
        pass

    @staticmethod
    def insert_new_line(input_string):
        pass

    @staticmethod
    def insert_format_string(input_string):
        
        pass

    @staticmethod
    def extend_string(input_string):
        extend_size = random.randint(0, 100000)
        mutated_string = input_string + ('A'*extend_size)
        return mutated_string

    @staticmethod
    def repeat_string(input_string):
        repeats = random.randint(0, 1000)
        mutated_string = input_string
        mutated_string = mutated_string*repeats
        return mutated_string

    @staticmethod
    def random_chars(input_string):
        num_replacements = random.randint(0, len(input_string) - 1)
        mutated_string = input_string
        for i in range(0, num_replacements):
                replacement_location = random.randint(0, len(input_string) - 1)
                replacement_character = chr(random.randint(0, 255))
                mutated_string = mutated_string[:replacement_location] + replacement_character + mutated_string[replacement_location + 1:]
        
        return mutated_string
    