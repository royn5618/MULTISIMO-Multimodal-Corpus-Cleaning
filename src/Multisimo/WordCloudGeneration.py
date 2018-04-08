'''
Created on 4 Apr 2018

@author: Owner
'''

import numpy as np # linear algebra
import pandas as pd 
import matplotlib as mpl
import matplotlib.pyplot as plt
from subprocess import check_output
from wordcloud import WordCloud, STOPWORDS
import wordcloud
from PIL import Image
from newspaper.nlp import stopwords

path = "../../clouds/"
df_withMod = pd.read_excel('../../Multisimo_Data/FullAndFinalData.xlsx')
df = df_withMod.iloc[3:]
df_Male = df.query('Gender_encoded == 0')
df_Female = df.query('Gender_encoded == 1')
circle_mask = np.array(Image.open("circle.png"))
#print(df_Male)
#print(df_Female)
colNames = ["EXTRAVERSION_en == 1", "AGREEABLENESS_en == 1" , "CONSCIENTIOUSNESS_en == 1",
            "NEUROTICISM_en == 1", "OPENNESS_en  == 1", "EXTRAVERSION_en == 0", "AGREEABLENESS_en == 0" , "CONSCIENTIOUSNESS_en == 0",
            "NEUROTICISM_en == 0", "OPENNESS_en  == 0"]
stopwords = ("dtype", "|", "Bu", "Cu", "Name", "Keywords", "object")


conversion_map = ({
    "laug": "laugh",
    "lAug": "laugh",
    "lAughhh" :"laugh",
    "Ah" : "Ah",
    "Eh" : "Ah",
    "Awh" : "Ah",
    "Uh" : "Ah",
    "a" : "A"
})


def _replace(df):
    i = 0;
    for index, row in df.iterrows():
        #row['Keywords']
        for k, v in conversion_map.items():
            line = row['Keywords'].replace(k, v)
            df.loc[index, 'Keywords'] = line
    return df


df_Male = _replace(df_Male)
df_Female = _replace(df_Female)

wordcloud = WordCloud(stopwords=stopwords,
                      background_color='white', mask=circle_mask,
                      max_words=500,
                      random_state=42
                     ).generate(str(df_Male['Keywords']))
fig = plt.figure(1)
plt.imshow(wordcloud)
plt.axis('off')
#plt.show()
fig.savefig(path+ "_male.png", dpi=900)

wordcloud = WordCloud(stopwords=stopwords,
                      background_color='white', mask=circle_mask,
                      max_words=500,
                      random_state=42
                     ).generate(str(df_Female['Keywords']))
fig = plt.figure(1)
plt.imshow(wordcloud)
plt.axis('off')
#plt.show()
fig.savefig(path + "_female.png", dpi=900)

'''
for eachBF in colNames:
    print(eachBF)
    df = df_Male.query(eachBF)
    wordcloud = WordCloud(stopwords=stopwords,
                          background_color='white', mask=circle_mask,
                          max_words=500,
                          random_state=42
                         ).generate(str(df['Keywords']))
    fig = plt.figure(1)
    plt.imshow(wordcloud)
    plt.axis('off')
    #plt.show()
    fig.savefig(path + eachBF +"_male.png", dpi=900)
    
for eachBF in colNames:
    print(eachBF)
    df = df_Female.query(eachBF)
    wordcloud = WordCloud(stopwords=stopwords,
                          background_color='white', mask=circle_mask,
                          max_words= 500,
                          random_state=42
                         ).generate(str(df['Keywords']))
    fig = plt.figure(1)
    plt.imshow(wordcloud)
    plt.axis('off')
    #plt.show()
    fig.savefig(path + eachBF +"female.png", dpi=900)'''



