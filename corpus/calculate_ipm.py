#this script calculates i.p.m (frequency per million words)
import codecs

file = "reflexive_total_parent_lemma_frequency.csv"
token_count_syn2015 = 120748715 #see https://wiki.korpus.cz/doku.php/cnk:syn2015
result = []

with codecs.open(file, encoding='utf-8') as f:
    for line in f:
        line = line.split(";")
        lemma = line[0]
        total_frequency = line[1]
        reflexive_frequency = line[2]
        reflexivity = line[3]
        total_ipm = (int(total_frequency)*1000000) / token_count_syn2015
        reflexive_ipm = (int(reflexive_frequency)*1000000) / token_count_syn2015
        result.append([lemma, total_frequency, str(total_ipm), reflexive_frequency, str(reflexive_ipm), reflexivity])
        
new_file="reflexive_parent_lemma_ipm.csv"
with open(new_file, 'a', encoding='utf-8') as f:
    for line in result:
        line = ';'.join(line)
        f.write(line)