from TypeMutator import TypeMutator
import sys
import random
class FloatMutator(TypeMutator):
    def __init__(self):
        pass
    
    #Note: these functions may require the float be rounded to nearest whole number first
    
    @staticmethod
    def bit_flip(flt):
        return ~flt
    
    @staticmethod
    def add_random(integer):
        integer += random.uniform(sys.minsize, sys.maxsize)
        return integer
    
    @staticmethod
    def sub_random(integer):
        integer -= random.uniform(sys.minsize, sys.maxsize)
        return integer
    
    @staticmethod
    def make_negative(flt):
        return -flt
    
    @staticmethod
    def make_huge(flt):
        return flt ** sys.maxsize
    
    @staticmethod
    def make_int(flt):
        return int(flt)
    
    @staticmethod
    def make_bool(flt):
        return bool(flt)
    
    @staticmethod
    def make_null():
        return None