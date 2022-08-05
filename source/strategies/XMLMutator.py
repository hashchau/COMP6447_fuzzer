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
    def mutate_once(payload):
        xml_tree = XMLMutator.get_xml_tree_from_xml_str(payload)
        rand_num = random.randint(0,2)
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
            # mutated_xml = "<tag>" * 35000 + "BREAD!" + "</tag>" * 35000
            mutated_xml = StringMutator.flip_bits(payload)
            print(f"mutated_xml: \n{mutated_xml}")
        
        return [mutated_xml]

    @staticmethod
    def mutate_all(payload):
        pass 
