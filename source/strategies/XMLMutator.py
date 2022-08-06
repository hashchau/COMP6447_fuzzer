import random
import xml.etree.ElementTree as ET

from .FormatMutator import FormatMutator                                                                                         
from .mutators.StringMutator import StringMutator

class XMLMutator(FormatMutator):
    @staticmethod
    def get_xml_tree_from_xml_str(xml_string):
        xml_tree = ET.ElementTree(ET.fromstring(xml_string))
        return xml_tree

    @staticmethod
    def get_xml_str_from_xml_tree(xml_tree):
        xml_root = xml_tree.getroot()
        xml_string = ET.tostring(xml_root, method='xml')
        xml_string = xml_string.decode('utf-8')
        return xml_string

    @staticmethod
    def mutate_once(default_payload, payload):
        try:
            rand_num = random.randint(0,3)
            # rand_num = 2
            if rand_num == 0:
                mutated_xml = XMLMutator.insert_format_str(payload)
            elif rand_num == 1:
                mutated_xml = XMLMutator.insert_many_columns_tags(payload)
            elif rand_num == 2:
                mutated_xml = XMLMutator.recurse_big()
            elif rand_num == 3:
                mutated_xml = XMLMutator.insert_bit_flip_on_value(payload)
            return [mutated_xml]
        except:
            return [default_payload]

    @staticmethod
    def recurse_big():
        return "<tag>" * 35000 + "BREAD!" + "</tag>" * 35000

    def insert_format_str(payload):
        xml_tree = XMLMutator.get_xml_tree_from_xml_str(payload)
        for child_ele in xml_tree.iter():
            if child_ele.attrib:
                key = list(child_ele.attrib.keys())[0]
                value = list(child_ele.attrib.values())[0]
                child_ele.set(key, value + StringMutator.insert_format_string(value))
        return XMLMutator.get_xml_str_from_xml_tree(xml_tree)

    def insert_bit_flip_on_value(payload):
        xml_tree = XMLMutator.get_xml_tree_from_xml_str(payload)
        for child_ele in xml_tree.iter():
            if child_ele.attrib:
                key = list(child_ele.attrib.keys())[0]
                value = list(child_ele.attrib.values())[0]
                child_ele.set(key, StringMutator.flip_bits(value))
                break
        return XMLMutator.get_xml_str_from_xml_tree(xml_tree)


    def insert_many_columns_tags(payload):
        xml_tree = XMLMutator.get_xml_tree_from_xml_str(payload)
        new_field_ele = ET.Element("field")
        xml_root = xml_tree.getroot()
        for i in range(50):
            ET.SubElement(new_field_ele, "column")
        xml_root.insert(1, new_field_ele)
        return XMLMutator.get_xml_str_from_xml_tree(xml_tree)