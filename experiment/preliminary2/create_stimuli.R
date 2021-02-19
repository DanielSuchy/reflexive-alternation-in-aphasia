library(tidyverse)
library(data.table)

sentences <- read.csv("sentence_group_2.csv", encoding = "UTF-8", sep=";")

#put each sentence in a separate row
sents_in_rows <- sentences %>% pivot_longer(c(transitive.grammatical, transitive.agrammatical, reflexive.grammatical, 
                                     reflexive.agrammatical), 
                                     values_to = "Sentence",
                                     names_to = "ItemType"
                                   )

#grammatical sentences are TRUE, otherwise FALSE
sents_in_rows$answer <- with(sents_in_rows, ifelse(ItemType %like% "e.grammatical", T, F))

#assign group to each sentence
#latin square design - each participant gets equal number of sentences from each type
#so let's say a single gram. trans sentece, single gram refl sentence and so on if we have four sentences types
#but we have 16 sentence types, so let's use this pattern 4 times
sents_in_rows <- sents_in_rows[order(sents_in_rows$lemma),] #to keep lemmas together
groups <- c("B", "C", "D", "A", #each lemma gets one from each group
            "C", "D", "A", "B",
            "D", "A", "B", "C",
            "A", "B", "C", "D"
            )
#groups <- c("A", "B", "C", "D", #each lemma gets one from each group
#            "B", "C", "D", "A",
#            "C", "D", "A", "B",
#            "D", "A", "B", "C"
#            )
pattern <- rep(groups, times = 4)
sents_in_rows$group <- pattern

#create an unique id to use in pcibex
sents_in_rows$item <- sents_in_rows$lemma_arguments_id
sents_in_rows$item <- with(sents_in_rows, ifelse(ItemType %like% "transitive.grammatical", paste0(sents_in_rows$item,"_TG"), sents_in_rows$item))
sents_in_rows$item <- with(sents_in_rows, ifelse(ItemType %like% "transitive.agrammatical", paste0(sents_in_rows$item,"_TA"), sents_in_rows$item))
sents_in_rows$item <- with(sents_in_rows, ifelse(ItemType %like% "reflexive.grammatical", paste0(sents_in_rows$item,"_RG"), sents_in_rows$item))
sents_in_rows$item <- with(sents_in_rows, ifelse(ItemType %like% "reflexive.agrammatical", paste0(sents_in_rows$item,"_RA"), sents_in_rows$item))

sents_in_rows$transitive <- with(sents_in_rows, ifelse(ItemType %like% "transitive", TRUE, FALSE))
sents_in_rows$grammatical <- with(sents_in_rows, ifelse(ItemType %like% "agrammatical", FALSE, TRUE))

#keep quotes just for this variable
sents_in_rows$Sentence <- paste0('"', sents_in_rows$Sentence, '"')

#save just the relevant columns
stimuli <- data.frame(Sentence = sents_in_rows$Sentence,
                      Answer = sents_in_rows$answer,
                      Group = sents_in_rows$group,
                      Item = sents_in_rows$item,
                      ArgumentVariation = paste0(sents_in_rows$lemma, "-2"),
                      Transitive = sents_in_rows$transitive,
                      Grammatical = sents_in_rows$grammatical)
write.csv(stimuli, "stimuli2.csv", fileEncoding = "UTF-8", row.names = F, quote = F)