import json
import yaml
import xml.etree.ElementTree as tree
import os
import xml.dom.minidom as dm 

class FileParser():

    def json_parser(self,path):
        #open file to read
        raw_json = open(path).read()
        #parsing the raw data
        parsed_json = json.loads(raw_json)
        return parsed_json
    
    def xml_parser(self,path):
        #open file to read
        raw_xml = tree.parse(path)
        '''
        raw_xml = dm.parse(open(path))
        print(type(raw_xml))
        root = raw_xml.getElementsByTagName('root')
        root = raw_xml.getroot()
        for child in root:
            print(child.tag,child.attrib)
        #print(root)
        #print(root[0].toxml())
        raw_xml = tree.parse(self.path)
        '''
        root = raw_xml.getroot()
        parsed_xml ={}
        for child in root:
            amount ={}
            for data in child:
                amount[data.tag] = data.text
            parsed_xml[child.tag] = amount
        return parsed_xml
    def yml_parser(self,path):
        raw_yml = open(path)
        return yaml.load(raw_yml)
if __name__ == '__main__':
    #parsedData = FileParser.json_parser('../data/db.json')
    parseData = FileParser()
    listData = []
    Jsondata = parseData.json_parser('../data/db.json')
    listData.append(Jsondata)
    Xmldata = parseData.xml_parser('../data/db.xml')
    listData.append(Xmldata)
    Ymldata = parseData.yml_parser('../data/db.yml')
    listData.append(Ymldata)
    print("Account Information")
    for data in listData:
        for account in data:
            print("Account Number",account)
            print("Due",data[account]['due'])
            print("Paid",data[account]['paid'])
            

    
    



