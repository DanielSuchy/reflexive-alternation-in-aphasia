#find verbs that are both reflexive and transitive and match them with their total frequency
library(tidyverse)

all <- read.csv("all_verbs_ipm.csv", encoding="UTF-8")
transitive <- read.csv("transitive_verbs_ipm.csv", encoding="UTF-8")
reflexive <- read.csv("reflexive_verbs_ipm.csv", encoding="UTF-8")

#these verbs occur in both transitive and reflexive lists
both_transitive_and_reflexive <- merge(transitive, reflexive, by = "lemma")
both_transitive_and_reflexive <-  both_transitive_and_reflexive %>% 
    rename(
        transitive_rank = order.x,
        reflexive_rank = order.y
    )

head(both_transitive_and_reflexive)

#merge them with list of all verbs to obtain their total frequency
target_verbs <- merge(both_transitive_and_reflexive, all, by = "lemma")
target_verbs <-  target_verbs %>% 
    rename(
        total_rank = order
    )

#for each verb, calculate how often it is used with a reflexive
target_verbs$refexivity <- (target_verbs$reflexive_frequency / target_verbs$total_frequency)
write.csv(target_verbs, "target_verbs_all.csv", fileEncoding = "UTF-8")

#most verbs are not realy reflexive, some are eclusively reflexive, few alternate
hist(target_verbs$refexivity)

#most reflexive verbs have very low frequency -> are unknown, we exclude them
#few have huge frequency - these are modal verbs, or highly abstact ones (be, have)
freq <- target_verbs$total_frequency[target_verbs$total_frequency > 1000]
freq <- freq[freq < 50000]
hist(freq) #there are only a few reflexive verbs, that occur frequently