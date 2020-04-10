import xml.etree.ElementTree as ET
import json
from collections import Counter

class Fils:

    def __init__(self, name='', item=0):
        self.list = []
        self.item = item
        self.data_list1 = []
        self.dropping_list = []
        self.name = name
        print(f"\n{self.name}\n")

    def list_open(self):

        if self.name == 'xml':
            for i in self.item:
                self.data_list1 = i.find("description").text.split()
                for word in self.data_list1:
                    if len(word) > 6:
                        self.dropping_list.append(word.lower())

            return self.dropping_list

        if self.name == 'json':
            for topic in self.item['rss']['channel']['items']:
                self.data_list1 = topic['description'].split()
                for word in self.data_list1:
                    if len(word) > 6:
                        self.dropping_list.append(word.lower())

            self.dropping_list

    def mortal(self):
        for mortal_word in Counter(self.dropping_list).most_common(10):
            print(f'слово "{mortal_word[0]}" встречается {mortal_word[1]} раз.')



parser1 = ET.XMLParser(encoding="utf-8")
tree1 = ET.parse(f"files/newsafr.xml", parser1)
root1 = tree1.getroot()
channel1 = root1.find("channel")
items1 = channel1.findall("item")

file1 = Fils('xml', items1)
file1.list_open()
file1.mortal()

with open(r"files/newsafr.json", encoding='utf-8', newline='') as f:
    data = json.load(f)

file2 = Fils('json', data)
file2.list_open()
file2.mortal()