import codecs

lemmas = '[lemma="dopouštět" | lemma="zmenšovat" | lemma="zobrazit" | lemma="zašklebit" | lemma="vyřešit" | lemma="tisknout" | lemma="přitisknout" | lemma="nechávat" | lemma="odtáhnout" | lemma="promítnout" | lemma="topit" | lemma="toulat" | lemma="poradit" | lemma="otvírat" | lemma="poprat" | lemma="splést" | lemma="myslet" | lemma="sehnout" | lemma="uzdravit" | lemma="prohánět" | lemma="zachytit" | lemma="zbavovat" | lemma="ukládat" | lemma="mihnout" | lemma="pohupovat" | lemma="zmenšit" | lemma="sebrat" | lemma="vysmívat" | lemma="vynořovat" | lemma="množit" | lemma="uvolňovat" | lemma="předklonit" | lemma="zachtít" | lemma="vytrácet" | lemma="uvažovat" | lemma="hromadit" | lemma="nosit" | lemma="rozbrečet" | lemma="zamyslit" | lemma="kouknout" | lemma="kroutit" | lemma="měřit" | lemma="odvolávat" | lemma="vléci" | lemma="propadat" | lemma="umět" | lemma="hroutit" | lemma="rozrůst" | lemma="ovládnout" | lemma="soudit" | lemma="nalézat" | lemma="rozcházet" | lemma="prolínat" | lemma="sevřít" | lemma="doslechnout" | lemma="zapojovat" | lemma="podrobit" | lemma="domáhat" | lemma="povalovat" | lemma="vyplácet" | lemma="převléknout" | lemma="ubytovat" | lemma="zachránit" | lemma="namáhat" | lemma="zamýšlet" | lemma="použít" | lemma="svléknout" | lemma="povídat" | lemma="potřebovat" | lemma="plnit" | lemma="líbat" | lemma="spekulovat" | lemma="přizpůsobovat" | lemma="klást" | lemma="vlnit" | lemma="slušet" | lemma="linout" | lemma="zakládat" | lemma="vymanit" | lemma="stihnout" | lemma="pokládat" | lemma="stačit" | lemma="diskutovat" | lemma="stočit" | lemma="opít" | lemma="potácet" | lemma="rozléhat" | lemma="rozprostírat" | lemma="vloupat" | lemma="pořádat" | lemma="zakousnout" | lemma="vzepřít" | lemma="zaplést" | lemma="roztřást" | lemma="přít" | lemma="připojovat" | lemma="zvětšit" | lemma="uzavírat" | lemma="zdráhat" | lemma="přistihnout" ]'
lemmas = lemmas.replace("lemma", "")
lemmas = lemmas.replace("[", "")
lemmas = lemmas.replace("]", "")
lemmas = lemmas.replace("]", "")
lemmas = lemmas.replace("=", "")
lemmas_list = lemmas.split(" | ")

file = "total_parent_lemma_frequency_501_600.csv"
results = []
with codecs.open(file, encoding='utf-8') as f:
    for line in f:
        line = line.split(";")
        results.append(line[1])
        
print(len(lemmas_list))
print(len(results))

for lemma in lemmas_list:
    if lemma not in results:
        print("lemma not found " + lemma)
    