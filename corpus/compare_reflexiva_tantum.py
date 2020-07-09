import codecs

file = "reflexiva_tantum.txt"

with codecs.open(file, encoding='utf-8') as f:
    tantum = [row.replace("\r\n", "") for row in f]
    
file = "reflexive_total_parent_lemma_frequency.csv"

with codecs.open(file, encoding='utf-8') as f:
    all_reflexives = [row.split(";") for row in f]
    

result = []

for lemma, total_frequency, reflexive_frequency, reflexivity in all_reflexives:
    lemma = lemma.replace('"', '')
    lemma = lemma + " se"
    if lemma in tantum and '!' not in tantum:
        print(lemma, total_frequency, reflexive_frequency, reflexivity)
        result.append([lemma, total_frequency, reflexive_frequency, reflexivity])
    
print(result)

new_file = "reflexiva_tantum_scale.csv"
with open(new_file, 'a', encoding='utf-8') as f:
    for lemma, total_frequency, relative_frequency, reflexivity in result:
        f.write(lemma + ";" + total_frequency + ";" + relative_frequency + ';' + str(reflexivity) + "\n")