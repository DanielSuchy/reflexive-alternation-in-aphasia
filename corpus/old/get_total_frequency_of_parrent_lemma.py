#this script creates corpus queries for verbs with reflexive alternations

import codecs

file = "reflexive_parent_lemma_frequency.csv"
lemmas = []

with codecs.open(file, encoding='utf-8') as f:
    for line in f:
        lemma = line.split(";")[1]
        lemma = lemma.replace('"', "")
        lemmas.append(lemma)
        
query = "["

for lemma in lemmas[500:600]:
    query = query + "lemma=" + '"' + lemma + '"' + " | "
    i = i + 1    

    
query = query[0:-2] + "]"
print (query)
print (query.count('lemma'))