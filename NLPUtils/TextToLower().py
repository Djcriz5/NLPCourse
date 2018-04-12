import codecs

import pkg_resources

from NLPUtils import TextIO_helper

if __name__ == '__main__':

    name = input()
    doc = str.lower(TextIO_helper.read_plain_text("Resources_assets", name))
    f = TextIO_helper.create_raw_text("Resources_assets", "Lower_" + name)  # opens file with name of "test.txt"
    f.writelines(doc)
    f.close()
    #print(pkg_resources.resource_filename("Resources_assets", 'e960404.htm'))
    #print(codecs.open(pkg_resources.resource_filename("Resources_assets", 'e960404.htm'), "r", encoding='utf-8', errors='ignore').read())

