import xml.etree.ElementTree as ET

def parse(path):
    tree = ET.parse(path)
    root = tree.getroot()

    dictionary = {}

    for item in root:
        dictionary[item.tag] = item.attrib
    return dictionary
