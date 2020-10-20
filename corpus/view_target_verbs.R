library("readxl")

verbs <- read_excel("target_verbs_manual.xlsx")

compatible_verbs <- verbs[verbs$is_sem_compatible == 'T',]
causative_verbs <- compatible_verbs[compatible_verbs$is_anticausative == 'F',]

visual_verbs <- verbs[verbs$is_visual == 'T' & verbs$is_anticausative == 'F' & verbs$is_sem_compatible == 'T',]