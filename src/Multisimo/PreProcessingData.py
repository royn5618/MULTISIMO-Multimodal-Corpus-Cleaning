'''
Created on 26 Mar 2018

@author: Owner
'''
import pandas as pd
from nltk.tag import StanfordPOSTagger
from nltk.corpus import stopwords
import nltk
from textblob import TextBlob
from pandas import DataFrame
from pandas import ExcelWriter
                    
st = StanfordPOSTagger('C:/Users/Owner/eclipse-workspace/Multisimo/stanford-postagger-2018-02-27/stanford-postagger-2018-02-27/models/english-bidirectional-distsim.tagger'
                       ,path_to_jar='C:/Users/Owner/eclipse-workspace/Multisimo/stanford-postagger-2018-02-27/stanford-postagger-2018-02-27/stanford-postagger.jar')
df_proc = pd.read_excel('C:/Users/Owner/eclipse-workspace/Multisimo/Multisimo_Data/Processed_transcripts.xlsx')
transcripts = df_proc['test_set'].tolist()

words = set(nltk.corpus.words.words())
eng_stopwords = set(stopwords.words('english'))

sentiment_list = []
nouns_list = [] #NN*
verbs_list = [] #VB*
personal_pronoun_list = [] #PRP
possessive_pronoun_list = [] #PRP$
wh_list = [] #W*
interjection_list = [] #UH
conjunction_list = [] #CC

df_features = DataFrame(columns=('sentiment_score', 'nouns_list', 'verbs_list', 'personal_pronoun_list', 
                                 'possessive_pronoun_list',
                          'wh_list', 'interjection_list', 'conjunction_list', 'count_NN', 'count_VB', 'count_PRP', 'count_PRP1',
                        'count_WH', 'count_interjection', 'count_conjunction'))

for item in transcripts:
    splits = item.split()
    item_set = set(splits)
    item_remove_stopwords = item_set - eng_stopwords
    item_only_literals = item_remove_stopwords.intersection(words)
    pos_tagged = st.tag(item_only_literals)
    blob_sentiment = TextBlob(" ".join(str(x) for x in item_only_literals))
    sentiment_score = blob_sentiment.sentiment.polarity
    sentiment_list.append(sentiment_score)
    print('sentiment added')
    for each in pos_tagged:
        if 'NN' in each[1]:
            nouns_list.append(each[0])
        if 'VB' in each[1]:
            verbs_list.append(each[0])
        if 'PRP' in each[1]:
            personal_pronoun_list.append(each[0])
        if 'PRP$' in each[1]:
            possessive_pronoun_list.append(each[0])
        if 'W' in each[1]:
            wh_list.append(each[0])
        if 'UH' in each[1]:
            interjection_list.append(each[0])
        if 'CC' in each[1]:
            conjunction_list.append(each[0])
    count_NN = len(nouns_list)
    count_VB = len(verbs_list)
    count_PRP = len(personal_pronoun_list)
    count_PRP1 = len(possessive_pronoun_list)
    count_WH = len(wh_list)
    count_interjection = len(interjection_list)
    count_conjunction_list = len(conjunction_list)
    
    row_add = [sentiment_score, nouns_list, verbs_list, personal_pronoun_list, possessive_pronoun_list, wh_list, 
               interjection_list, conjunction_list, count_NN, count_VB, count_PRP, count_PRP1, count_WH,
               count_interjection, count_conjunction_list]
    print(row_add)
    df_features.loc[len(df_features)] = row_add
    print('row appended')
    
print(df_features)

writer = ExcelWriter('Features.xlsx')
df_features.to_excel(writer)
writer.save()
print('done')
    