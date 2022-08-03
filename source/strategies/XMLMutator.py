from re import M
from .FormatMutator import FormatMutator                                                                                         
from .mutators.StringMutator import StringMutator                                                                                       
from .mutators.IntegerMutator import IntegerMutator 
from pprint import pprint

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
    
    def unparse_xml(payload):
        xml = xmltodict.unparse(payload, pretty=True)
        xml = xml.splitlines()[1:]
        xml = '\n'.join(xml)
        return xml

    @staticmethod
    def mutate_once(payload):
        xml_dict = XMLMutator.parse_xml(payload)
        rand_num = 0
        print(f"trying strategy {rand_num}")
        if rand_num == 0:
            mutated_payload = XMLMutator.insert_format_string(xml_dict)
        # elif rand_num == 1:
        #     mutated_xml = XMLMutator.unparse_xml(payload)


        mutated_xml = XMLMutator.unparse_xml(mutated_payload)

        return [mutated_xml]

    @staticmethod
    def mutate_all(payload):
        pass 

    # @staticmethod
    # def insert_integer_overflow(payload):

    # @staticmethod
    # def insert_integer_underflow(payload):
    
    # @staticmethod
    # def insert_buffer_overflow(payload):

    @staticmethod
    def insert_single_format_specifier(payload):
        def format_string(value):
            if isinstance(value, str):
                return StringMutator.insert_single_format_specifier(value)

        return XMLMutator.apply_function_recursively(payload, format_string)

    def insert_format_string(payload):
        def format_string(value):
            if isinstance(value, str):
                return StringMutator.insert_format_string(value)

        return XMLMutator.apply_function_recursively(payload, format_string)
        
    @staticmethod
    # <hr></hr>
    def insert_xml_tag(payload):
        def xml_tag(value):
            mutated_value = value
            mutated_value += "<field>"
            for i in range(0, random.randint(1, 100)):
                mutated_value += "<column />"
            mutated_value += "</field>"
            return mutated_value
        return XMLMutator.apply_function_recursively(payload, xml_tag)

    @staticmethod
    def apply_function_recursively(obj, func):
        if obj is None:
            return None

        if not isinstance(obj, list) and not isinstance(obj, dict):
            return func(obj)
        
        if isinstance(obj, dict):
            for key, value in obj.items():
                obj[key] = XMLMutator.apply_function_recursively(value, func)
            # for key, value in obj.items():
            #     obj[XMLMutator.apply_function_recursively(key, func)] = value

        if isinstance(obj, list):
            for i, value in enumerate(obj):
                obj[i] = XMLMutator.apply_function_recursively(value, func)

        return obj
