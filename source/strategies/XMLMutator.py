from .FormatMutator import FormatMutator                                                                                         
from .mutators.StringMutator import StringMutator                                                                                       
from .mutators.IntegerMutator import IntegerMutator 
from pprint import pprint
from copy import deepcopy

import random
import xmltodict
import xml.etree.ElementTree as ET

class XMLMutator(FormatMutator):
    def get_xml_tree_from_xml_str(xml_string):
        xml_tree = ET.ElementTree(ET.fromstring(xml_string))
        return xml_tree

    def get_xml_str_from_xml_tree(xml_tree):
        xml_root = xml_tree.getroot()
        xml_string = ET.tostring(xml_root, method='xml')
        xml_string = xml_string.decode('utf-8')
        return xml_string

    @staticmethod
    def mutate_once(payload):
        xml_tree = XMLMutator.get_xml_tree_from_xml_str(payload)
        print(f"xml_tree type: {type(xml_tree)}")
        rand_num = random.randint(0,1)
        rand_num = 2
        print(f"Choosing strategy {rand_num}")
        if rand_num == 0:
            for child_ele in xml_tree.iter():
                if child_ele.attrib:
                    key = list(child_ele.attrib.keys())[0]
                    value = list(child_ele.attrib.values())[0]
                    value += "%s"
                    child_ele.set(key, value)
            mutated_xml = XMLMutator.get_xml_str_from_xml_tree(xml_tree)
        if rand_num == 1:
            new_field_ele = ET.Element("field")
            xml_root = xml_tree.getroot()
            for i in range (50):
                ET.SubElement(new_field_ele, "column")
            xml_root.insert(1, new_field_ele)
            mutated_xml = XMLMutator.get_xml_str_from_xml_tree(xml_tree)
        if rand_num == 2:
            # new_tag_ele = ET.Element("tag")
            # xml_root = xml_tree.getroot()
            # for i in range (1000):
            #     ET.SubElement(new_tag_ele, "tag")
            # xml_root.insert(0, new_tag_ele)
            mutated_xml = "<tag>" * 1000000 + "BREAD!" + "</tag>" * 1000000
        
        return [mutated_xml]

    @staticmethod
    def mutate_all(payload):
        pass 

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
