import re

# parse XML
# zoek de waarde van een xml element.
# field = element, xml = xml-data

def fieldvalue(field, xml):
    try:
        return re.search("(?s)<{}>(.*?)</{}>".format(field, field), xml).group(1)
    except AttributeError:
        return None

# parse XML.
# field = element you want to catch. xml is the xml-data.

def fieldvalues(field, xml):
    return re.findall("(?s)<{}>(.*?)</{}>".format(field,field), xml)
