import codecs
import random

file = "reflexive_total_parent_lemma_ipm.csv"


all_verbs = []
with codecs.open(file, encoding='utf-8') as f:
    for line in f:
        line = line.split(";")
        all_verbs.append(line)
        
def get_random_verbs(bottom, top):
    output = []
    random.shuffle(all_verbs)
    i = 0
    while len(output) != 20:
        random_verb = all_verbs[i]
        reflexivity = float(random_verb[5])
        if reflexivity > bottom and reflexivity < top:
            output.append(random_verb)
        i = i + 1
        
    return output

def write_random_verbs(verb_list):
    random_verbs = "random_verbs.csv"
    with open(random_verbs, 'a', encoding='utf-8') as f:
        for line in verb_list:
            line = ";".join(line)
            f.write(line)
    
reflexive_20 = get_random_verbs(0.15, 0.25)
reflexive_30 = get_random_verbs(0.25, 0.35)
reflexive_40 = get_random_verbs(0.35, 0.45)
reflexive_50 = get_random_verbs(0.45, 0.55)
reflexive_60 = get_random_verbs(0.55, 0.65)
reflexive_70 = get_random_verbs(0.65, 0.75)
reflexive_80 = get_random_verbs(0.75, 0.85)

write_random_verbs(reflexive_20)
write_random_verbs(reflexive_30)
write_random_verbs(reflexive_40)
write_random_verbs(reflexive_50)
write_random_verbs(reflexive_60)
write_random_verbs(reflexive_70)
write_random_verbs(reflexive_80)