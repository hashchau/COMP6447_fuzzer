from .FormatMutator import FormatMutator                                                                                         
from .mutators.StringMutator import StringMutator                                                                                       
from .mutators.IntegerMutator import IntegerMutator 

import json

class XMLMutator(FormatMutator):
    @staticmethod
    def mutate_once(payload):

    @staticmethod
    def mutate_all(payload):

    @staticmethod
    def insert_integer_overflow(payload):

    @staticmethod
    def insert_integer_underflow(payload):

    @staticmethod
    def insert_format_string(payload):

    @staticmethod
    def insert_buffer_overflow(payload):

    @staticmethod
    def apply_function_recursively(obj, func):
