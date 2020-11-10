## danovo data

library(tidyr)
library(dplyr)
library(ggplot2)

df <- read.csv("target_verbs_manual.csv", encoding = "UTF-8")

glimpse(df)

refl_density <- df %>% filter(is_sem_compatible == T & is_anticausative == F) %>% ggplot(aes(x = reflexivity)) + geom_density()

refl_density

## just eyeballing: refl low ~ .2-.3 & refl h ~ .6-.8

ipm_density <- df %>% filter(is_sem_compatible == T & is_anticausative == F) %>% ggplot(aes(x = total_ipm)) + geom_density()

ipm_density

df %>% filter(is_sem_compatible == T & is_anticausative == F) %>% summary()

## nums of candidate lemmas

df %>% filter(is_sem_compatible == T & is_anticausative == F & reflexivity <= .3 & total_ipm <= 100) %>% nrow

df %>% filter(is_sem_compatible == T & is_anticausative == F & reflexivity >= .59 & total_ipm <= 100) %>% nrow

candidate_lemmas <- df %>% filter(is_sem_compatible == T & is_anticausative == F & total_ipm <= 100 & (reflexivity <= .3 | reflexivity >= .59))

candidate_lemmas <- candidate_lemmas %>% mutate(refl.bias = if_else(reflexivity <= .3, "low", "high"))

#write_csv(candidate_lemmas, "c:/Users/lazni/Desktop/dan_candidate_lemmas.csv")

n_ok <- df %>% filter(total_ipm <= 100 & (is_sem_compatible == F | is_anticausative == T)) %>% mutate(refl.bias = if_else(reflexivity <= .3, "low", if_else(reflexivity >= .59, "high", "neu")))

#write_csv(n_ok, "c:/Users/lazni/Desktop/dan_n_ok_lemmas.csv")
