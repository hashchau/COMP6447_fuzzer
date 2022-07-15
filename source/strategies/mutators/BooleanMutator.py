from TypeMutator import TypeMutator
class BooleanMutator(TypeMutator):
    def __init__(self):
        pass
    
    @staticmethod
    def boolean_flip(boolean):
        return not boolean
    
    @staticmethod
    def boolean_to_string(boolean):
        return str(boolean)
    
    @staticmethod
    def boolean_to_int(boolean):
        return int(boolean)
    
    @staticmethod
    def boolean_to_float(boolean):
        return float(boolean)
