from hamcrest import none
from .TypeMutator import TypeMutator
import sys
import random
class FloatMutator(TypeMutator):
    #Note: these functions may require the float be rounded to nearest whole number first
    
    @staticmethod
    def add_random(flt):
        flt += random.uniform(-(sys.maxsize - 1), sys.maxsize)
        return flt
    
    @staticmethod
    def sub_random(flt):
        flt -= random.uniform(-(sys.maxsize - 1), sys.maxsize)
        return flt
    
    @staticmethod
    def make_negative(flt):
        return -flt
    
    @staticmethod
    def make_huge(flt):
        return float('inf')
    
    @staticmethod
    def make_tiny(flt):
        return float('-inf')

    @staticmethod
    def make_int(flt):
        return int(flt)
    
    @staticmethod
    def make_bool(flt):
        return bool(flt)
    
    @staticmethod
    def make_null():
        return float("NaN")
    
    @staticmethod
    def is_float(input_string):
        if isinstance(input_string, str):
            s = input_string.lstrip("-")
            return ('.' in s) and (s.replace('.', '', 1).isdigit())
        
        return isinstance(input_string, float)