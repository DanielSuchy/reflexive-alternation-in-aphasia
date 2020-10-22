This folder includes scripts and data related to the corpus research  

## Description of files  
all_verbs.csv - list of all verb lemmas in the corpus, with their frequencies  
all_verbs_ipm.csv - same as all_verbs, but with ipm without punctuation  
transitive_verbs.csv - list of all verb lemmas in the corpus, that are a syntactic parent to a noun in accusative  
reflexive_verbs.csv - list of all verb lemmas in the corpus, that are a syntactic parent to a reflexive particle  
target_verbs_all.csv - union of transitive, reflexive and total lists. Added reflexivity, as a ratio between total and reflexive use.  
target_verbs_filtered.csv - shorter list, target verbs filtered by reflexivity (around average) and absolute frequency (high, but not extremely high)  
target_verbs_manual.xlsx - filtered verbs, manually annotated for:  
	is_sem_compatible - T if verb is semantically compatible / reversible in reflexive alternation. Both alternations have troughly the same meaning.  
	is_anticausative - passive form of the verb usally has an anticausative function  
	uses_double_accusative - transitive verb form is typically used with two arguments in accusative  
	is_visual - refers to an action that can be easily visualised (e.g. refered to with a simple drawning)  
	