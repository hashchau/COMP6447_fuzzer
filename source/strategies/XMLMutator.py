from .FormatMutator import FormatMutator                                                                                         
from .mutators.StringMutator import StringMutator                                                                                       
from .mutators.IntegerMutator import IntegerMutator 

import random
import xmltodict
# import xml.etree.ElementTree as ET

class XMLMutator(FormatMutator):
    # def parse_xml(xml_string):
    #     xml_root = ET.fromstring(xml_string)
    #     return xml_root

    # def unparse_xml(xml_root):
    #     xml_string = ET.tostring(xml_root, method='xml')
    #     return xml_string

    def parse_xml(payload):
        xml_dict = xmltodict.parse(payload)
        return xml_dict

    @staticmethod
    def mutate_once(payload):
        xml_dict = XMLMutator.parse_xml(payload)
        rand_num = randint(0,2)
        pass 

    @staticmethod
    def mutate_all(payload):
        pass 

    # @staticmethod
    # def insert_integer_overflow(payload):

    # @staticmethod
    # def insert_integer_underflow(payload):

    # @staticmethod
    # def insert_format_string(payload):

    # @staticmethod
    # def insert_buffer_overflow(payload):

    # @staticmethod
    # def apply_function_recursively(obj, func):
