from .TypeMutator import TypeMutator
import sys
import random
class IntegerMutator(TypeMutator):
    @staticmethod
    def bit_flip(integer):
        return ~integer
    
    @staticmethod
    def add_random(integer):
        integer += random.randint(0, 65535)
        return integer
    
    @staticmethod
    def sub_random(integer):
        integer -= random.randint(0, 65535)
        return integer
    
    @staticmethod
    def make_negative(integer):
        return -integer
    
    @staticmethod
    def make_huge(integer):
        return sys.maxsize
    
    @staticmethod
    def make_tiny(integer):
        return -(sys.maxsize)
        
    @staticmethod
    def make_float(integer):
        return float(integer)
    
    @staticmethod
    def make_bool(integer):
        return bool(integer)
    
    @staticmethod
    def make_null():
        return None

    @staticmethod
    def is_integer(input_string):
        if isinstance(input_string, str):
            return input_string.lstrip("-").isdigit()
        
        return isinstance(input_string, int)