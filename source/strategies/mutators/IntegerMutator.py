from TypeMutator import TypeMutator
import sys
class IntegerMutator(TypeMutator):
    def __init__(self):
        pass
    
    @staticmethod
    def bit_flip(integer):
        return ~integer
    
    @staticmethod
    def make_negative(integer):
        return -integer
    
    @staticmethod
    def make_huge(integer):
        return integer ** sys.maxsize
    
    @staticmethod
    def make_float(integer):
        return float(integer)
    
    @staticmethod
    def make_bool(integer):
        return bool(integer)
