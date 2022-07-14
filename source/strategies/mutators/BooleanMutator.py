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
        result = [1 if boolean is True else 0]
        return result
