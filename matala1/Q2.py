# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 11:11:46 2023

@author: berber
"""
#Matala 1 - Q2



def revword(word:str):
    new_word = word[::-1] #[from begin:to end:-1 -> reverse]
    return new_word.lower().strip()
#testing:
print(revword('Divad'))


def countword(file_name):
    file=open(file_name)
    counter=1 #=1 because its include first word
    for line in file:
        words=line.split(" ") #split by spaces
        if len(words)==1: #first word needs to be saved as variable
            word=words[0].lower().strip()
        for w in words:
            w=revword(w)
            if w==word:
                counter+=1
    return word, counter

#testing:
print(countword('text.txt'))        
        
