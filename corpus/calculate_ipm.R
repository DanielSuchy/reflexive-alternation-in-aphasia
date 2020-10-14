#this script calculates ipm (frequency per million words) from absolute frequency in a corpus
#input is a list of lemmas with absolute frequencies

token_count <- 100838568 #token count of syn2015 corpus, without punctuation
#token2 <- 120748715
lemmas <- read.csv("reflexive_verbs.csv", encoding="UTF-8")

lemmas$ipm <- (lemmas$frequency * 1000000) / token_count #as described in http://www.thegrammarlab.com/?p=160

lemmas[] #this ipm is slightly different from the default in corpus app, bc. we ignore punctuation

write.csv(lemmas, "reflexive_verbs_ipm.csv", fileEncoding = "UTF-8")