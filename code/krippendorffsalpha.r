library(gdata)
ratings <- read.xls('/home/jvdzwaan/data/dilipad/results/all_years-adj-cabinets_selected-parties/topics_100.xlsx')
usef <- ratings[c("usefulness_A", "usefulness_B", "usefulness_C")]
#ratings <- read.csv('/home/jvdzwaan/data/dilipad/results/all_years-adj-cabinets_selected-parties/topic_coherence_100.csv')
#usef <- ratings[c("ca", "cp", "cv", "npmi", "uci", "umass")]
library('irr')
library('base')
kripp.alpha(t(data.matrix(usef)), method='ordinal')