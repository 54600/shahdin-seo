from flask import Flask,jsonify,request
import requests
from bs4 import BeautifulSoup
import re
import nltk
from nltk.corpus import wordnet
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords 
import random

stop_words = stopwords.words("english") 

def plagiarism_remover(i):
    word = i
    synonyms = []
    if word in stop_words:
        return word
    if wordnet.synsets(word)==[]:
        return word
    for syn in wordnet.synsets(word):
        for lemma in syn.lemmas():
            synonyms.append(lemma.name())
    pos_tag_word = nltk.pos_tag([word])
    pos = []
    for i in synonyms:
        pos.append(nltk.pos_tag([i]))
    final_synonyms = []
    for i in pos:
        if pos_tag_word[0][1] == i[0][1]:
            final_synonyms.append(i[0][0])
    final_synonyms = list(set(final_synonyms))
    if final_synonyms == []:
        return word
    if word.istitle():
        return random.choice(final_synonyms).title()
    else:
        return random.choice(final_synonyms)
    
def plagiarism_removal(para):
    para_split = word_tokenize(para)
    final_text = []
    for i in para_split:
        final_text.append(plagiarism_remover(i))
    final_text = " ".join(final_text)
    #final_text = final_text.replace("_","<span style='color:transparent'>_</span>")
    final_text = final_text.replace("_"," ")
    
    return final_text
# def correct_grammer(content):
#     from gingerit.gingerit import GingerIt
#   text = input("Enter a sentence >>: ")
# corrected_text = GingerIt().parse(text)
# print(corrected_text['result'])
