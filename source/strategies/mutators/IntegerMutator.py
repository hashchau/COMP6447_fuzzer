from .TypeMutator import TypeMutator
import sys
import random
class IntegerMutator(TypeMutator):
    
    @staticmethod
    def bit_flip(integer):
        return ~integer
    
    @staticmethod
    def add_random(integer):
        integer += random.randint(sys.minsize, sys.maxsize)
        return integer
    
    @staticmethod
    def sub_random(integer):
        integer -= random.randint(sys.minsize, sys.maxsize)
        return integer
    
    @staticmethod
    def make_negative(integer):
        return -integer
    
    @staticmethod
    def make_huge(integer):
        return sys.maxsize
        # max_signed_32_bit_integer = 2147483647
        # return max_signed_32_bit_integer
    
    @staticmethod
    def make_tiny(integer):
        return -(sys.maxsize)
        # min_signed_32_bit_integer = -2147483648
        # return min_signed_32_bit_integer
    
    @staticmethod
    def make_float(integer):
        return float(integer)
    
    @staticmethod
    def make_bool(integer):
        return bool(integer)
    
    @staticmethod
    def make_null():
        return None
