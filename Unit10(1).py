from collections import Counter
import xml.etree.ElementTree as ET
import json

print("\n Для json \n")
word_list = []


with open(r"files/newsafr.json", encoding='utf-8', newline='') as f:
    data = json.load(f)

for topic in data['rss']['channel']['items']:
    common_list = topic['description'].split()
    for word in common_list:
               if len(word) > 6:


                   word_list.append(word.lower())

for long_word in Counter(word_list).most_common(10):

    print(f'слово "{long_word[0]}" встречается {long_word[1]} раз.')



print("\n Для xml \n")


dropping_list = []

parser = ET.XMLParser(encoding="utf-8")
tree = ET.parse(f"files/newsafr.xml", parser)
root = tree.getroot()
channel = root.find("channel")
items = channel.findall("item")
for item in items:
    data_list = item.find("description").text.split()
    for word in data_list:
        if len(word) > 6:
            dropping_list.append(word)

for mortal_word in Counter(dropping_list).most_common(10):
    print(f'слово "{mortal_word[0]}" встречается {mortal_word[1]} раз.')






