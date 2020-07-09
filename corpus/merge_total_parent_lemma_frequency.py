#this script merges the results of small corpus queries into one

import codecs
import os

verbs = []

for file in os.listdir("."): 
    if file.startswith("total") and file.endswith("00.csv"):
        with codecs.open(file, encoding='utf-8') as f:
            for line in f:
                line.replace("\n", "")
                verbs.append(line.rstrip())

new_file = "total_parent_lemma_frequency.csv"
with open(new_file, 'a', encoding='utf-8') as f:
    for line in verbs:
        f.write(line + '\n')