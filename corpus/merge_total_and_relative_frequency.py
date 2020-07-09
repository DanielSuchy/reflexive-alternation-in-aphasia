import codecs

total_frequency_csv = "total_parent_lemma_frequency.csv"
reflexive_frequency_csv = "reflexive_parent_lemma_frequency.csv"

def get_lemma_frequency(row, result):
    row = row.split(";")
    if row[0] != '"xx"':
        lemma = row[1]
        frequency = row[2]
        result.append([lemma, frequency])
    

total_frequency_list = []
with codecs.open(total_frequency_csv, encoding='utf-8') as f:
    for row in f:
        get_lemma_frequency(row, total_frequency_list)
    
reflexive_frequency_list = []
with codecs.open(reflexive_frequency_csv, encoding='utf-8') as f:
    for row in f:
        get_lemma_frequency(row, reflexive_frequency_list)
        
result = []
for lemma, total_frequency in total_frequency_list:
    for reflexive_lemma, reflexive_frequency in reflexive_frequency_list:
        if reflexive_lemma == lemma:
            total_frequency = total_frequency.replace('"', '')
            reflexive_frequency = reflexive_frequency.replace('"', '')
            result.append([lemma, total_frequency, reflexive_frequency])

new_file = "reflexive_total_parent_lemma_frequency.csv"
with open(new_file, 'a', encoding='utf-8') as f:
    for lemma, total_frequency, relative_frequency in result:
        reflexivity = int(relative_frequency) / int(total_frequency)
        print(lemma, total_frequency, relative_frequency, reflexivity)
        f.write(lemma + ";" + total_frequency + ";" + relative_frequency + ';' + str(reflexivity) + "\n")